# https://github.com/ram133/open-webui-cloud
import urllib.request
import urllib.parse
import json
import os
import datetime

BOTS = [
    {
        "name": "TEXCOOLBot",
        "token": "7464269358:AAEcUuwyX77QOAh6i_NJyPcYfNfhLreu3Lw",
        "url": "https://ray2407.github.io/texcool",
        "description": "TEXCOOL Portal & Web Tools"
    },
    {
        "name": "Ray2FB Bot",
        "token": "8056349243:AAH7CVgBx5_ese73xjCg3ah71T6-NlrOeaI",
        "url": "https://ray2407.github.io/ray2fb",
        "description": "Ray2FB Publishing Tools"
    },
    {
        "name": "0724 Bot",
        "token": "7355656881:AAEe3hHYjDAlg6aVQ8Iw8M125qxqBxlnYK4",
        "url": "https://ray2407.github.io/0724",
        "description": "0724 Digital Hub"
    },
    {
        "name": "RayoR",
        "token": "7942570289:AAGYVe68mlMo14qXfDLEXhDInOhAcnVvhPA",
        "url": "https://ram133.github.io/open-webui-cloud/",
        "description": "Open WebUI Cloud & Central Hub"
    }
]

def setup_bot_commands(token):
    url = f"https://api.telegram.org/bot{token}/setMyCommands"
    commands = [
        {"command": "start", "description": "Open main menu & portal"},
        {"command": "portal", "description": "Launch Web App in Telegram"},
        {"command": "pricing", "description": "View hourly services & pricing"},
        {"command": "support", "description": "Get direct support contact"}
    ]
    payload = urllib.parse.urlencode({"commands": json.dumps(commands)}).encode('utf-8')
    try:
        urllib.request.urlopen(urllib.request.Request(url, data=payload, method="POST"), timeout=5)
    except Exception:
        pass

def send_webapp_message(token, chat_id, bot_info):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    keyboard = {
        "inline_keyboard": [
            [
                {"text": "🚀 Launch Web App", "web_app": {"url": bot_info["url"]}},
                {"text": "📂 Central Hub", "url": "https://ram133.github.io/open-webui-cloud/"}
            ],
            [
                {"text": "💳 Hourly Services", "url": "https://www.ray.services/work/index.php"},
                {"text": "📞 Support", "url": "mailto:crh2509@icloud.com"}
            ]
        ]
    }
    
    payload = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": f"🤖 *{bot_info['name']}*\n\n_{bot_info['description']}_\n\nTap below to launch the native Web App or explore central tools:",
        "parse_mode": "Markdown",
        "reply_markup": json.dumps(keyboard)
    }).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=payload, method="POST")
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode('utf-8')).get("ok", False)
    except Exception:
        return False

def handle_incoming(bot):
    token = bot["token"]
    setup_bot_commands(token)
    
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
                    if msg and "text" in msg and "chat" in msg:
                        chat_id = msg["chat"]["id"]
                        text = msg["text"].strip().lower()
                        
                        success = send_webapp_message(token, chat_id, bot)
                        events.append({
                            "chat_id": chat_id,
                            "text": text,
                            "response_sent": success
                        })
    except Exception as e:
        print(f"Error handling {bot['name']}: {e}")
    return events

if __name__ == "__main__":
    print("Running Advanced WebApp Telegram Daemon...")
    report = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "bots_checked": len(BOTS),
        "activity": {}
    }
    
    total_interactions = 0
    for bot in BOTS:
        events = handle_incoming(bot)
        report["activity"][bot["name"]] = events
        total_interactions += len(events)
        
    report["total_interactions"] = total_interactions
    
    with open("run_report.json", "w") as f:
        json.dump(report, f, indent=2)
        
    print(f"Polling Complete. Total interactions processed: {total_interactions}")
