# https://github.com/ram133/open-webui-cloud
import urllib.request
import urllib.parse
import json
import os
import datetime
import random

BOTS = [
    {"name": "TEXCOOLBot", "token": "7464269358:AAEcUuwyX77QOAh6i_NJyPcYfNfhLreu3Lw", "url": "https://ray2407.github.io/texcool", "description": "TEXCOOL Portal"},
    {"name": "Ray2FB Bot", "token": "8056349243:AAH7CVgBx5_ese73xjCg3ah71T6-NlrOeaI", "url": "https://ray2407.github.io/ray2fb", "description": "Ray2FB Tools"},
    {"name": "0724 Bot", "token": "7355656881:AAEe3hHYjDAlg6aVQ8Iw8M125qxqBxlnYK4", "url": "https://ray2407.github.io/0724", "description": "0724 Hub"},
    {"name": "RayoR", "token": "7942570289:AAGYVe68mlMo14qXfDLEXhDInOhAcnVvhPA", "url": "https://ram133.github.io/open-webui-cloud/", "description": "Open WebUI Cloud"}
]

LEADS_FILE = "leads.json"

SALES_PITCHES = [
    "🔥 *Storefront Drop:* Get our 4-Bot SaaS Fleet Source Code for instant deployment!",
    "⚡ *Developer Special:* Download single-file PWA boilerplates from our Digital Vault.",
    "🚀 *Scale Faster:* Book direct engineering hours or grab automated workflow scripts."
]

def load_leads():
    if os.path.exists(LEADS_FILE):
        try:
            with open(LEADS_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            pass
    return {"chats": [], "total_interactions": 0}

def save_leads(data):
    with open(LEADS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def send_sales_message(token, chat_id, bot_info):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    pitch = random.choice(SALES_PITCHES)
    
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "🛍️ Visit Digital Vault Store", "web_app": {"url": "https://ram133.github.io/open-webui-cloud/store.html"}},
                {"text": "💳 Book Hourly Work", "url": "https://www.ray.services/work/index.php"}
            ],
            [
                {"text": "🚀 Launch Web App", "web_app": {"url": bot_info["url"]}},
                {"text": "📞 Support / Signal", "url": "https://signal.me/#u/iknowme.08"}
            ]
        ]
    }
    
    payload = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": f"🤖 *{bot_info['name']} (Revenue Engine)*\n\n{pitch}\n\nTap below to browse instant assets or secure services:",
        "parse_mode": "Markdown",
        "reply_markup": json.dumps(keyboard)
    }).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=payload, method="POST")
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode('utf-8')).get("ok", False)
    except Exception:
        return False

def handle_incoming(bot, leads_db):
    token = bot["token"]
    url = f"https://api.telegram.org/bot{token}/getUpdates?timeout=2"
    events = []
    
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data.get("ok"):
                for result in data.get("result", []):
                    update_id = result["update_id"]
                    urllib.request.urlopen(f"https://api.telegram.org/bot{token}/getUpdates?offset={update_id + 1}&timeout=1")
                    
                    msg = result.get("message") or result.get("edited_message")
                    if msg and "chat" in msg:
                        chat_id = str(msg["chat"]["id"])
                        if chat_id not in leads_db["chats"]:
                            leads_db["chats"].append(chat_id)
                        leads_db["total_interactions"] += 1
                        
                        success = send_sales_message(token, chat_id, bot)
                        events.append({"bot": bot["name"], "chat_id": chat_id, "success": success})
    except Exception as e:
        print(f"Error: {e}")
    return events

if __name__ == "__main__":
    leads_db = load_leads()
    report = {"timestamp": datetime.datetime.utcnow().isoformat() + "Z", "activity": {}}
    total = 0
    for bot in BOTS:
        events = handle_incoming(bot, leads_db)
        report["activity"][bot["name"]] = events
        total += len(events)
    report["total_interactions"] = total
    report["total_unique_leads"] = len(leads_db["chats"])
    save_leads(leads_db)
    with open("run_report.json", "w") as f:
        json.dump(report, f, indent=2)
