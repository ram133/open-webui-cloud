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
        "response": "🚀 TEXCOOL Portal: https://ray2407.github.io/texcool\nSupport: crh2509@icloud.com"
    },
    {
        "name": "Ray2FB Bot",
        "token": "8056349243:AAH7CVgBx5_ese73xjCg3ah71T6-NlrOeaI",
        "response": "🚀 Ray2FB Portal: https://ray2407.github.io/ray2fb\nSupport: crh2509@icloud.com"
    },
    {
        "name": "0724 Bot",
        "token": "7355656881:AAEe3hHYjDAlg6aVQ8Iw8M125qxqBxlnYK4",
        "response": "🚀 0724 Portal: https://ray2407.github.io/0724\nSupport: crh2509@icloud.com"
    },
    {
        "name": "RayoR",
        "token": "7942570289:AAGYVe68mlMo14qXfDLEXhDInOhAcnVvhPA",
        "response": "🚀 Open WebUI Cloud: https://ram133.github.io/open-webui-cloud/\nSupport: crh2509@icloud.com"
    }
]

KEYWORDS = ["openwebui", "texcool", "ray2fb", "0724", "cloud", "github", "deploy", "ai", "bot"]

def send_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }).encode('utf-8')
    try:
        req = urllib.request.Request(url, data=payload, method="POST")
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode('utf-8')).get("ok", False)
    except Exception:
        return False

def poll_bot(bot):
    token = bot["token"]
    url = f"https://api.telegram.org/bot{token}/getUpdates?timeout=2"
    matched_events = []
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
                        text = msg["text"].lower()
                        if any(kw in text for kw in KEYWORDS):
                            success = send_message(token, chat_id, bot["response"])
                            matched_events.append({
                                "chat_id": chat_id,
                                "text": msg["text"],
                                "matched": True,
                                "response_sent": success
                            })
    except Exception as e:
        print(f"Error polling {bot['name']}: {e}")
    return matched_events

if __name__ == "__main__":
    print("Running Cloud Telegram Polling Pass...")
    report = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "bots_checked": len(BOTS),
        "activity": {}
    }
    
    total_matches = 0
    for bot in BOTS:
        events = poll_bot(bot)
        report["activity"][bot["name"]] = events
        total_matches += len(events)
        
    report["total_matches"] = total_matches
    
    with open("run_report.json", "w") as f:
        json.dump(report, f, indent=2)
        
    print(f"Polling Complete. Total keyword matches processed: {total_matches}")
