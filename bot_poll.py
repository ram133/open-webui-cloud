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

def handle_incoming(bot):
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
                    if msg and "text" in msg and "chat" in msg:
                        chat_id = msg["chat"]["id"]
                        text = msg["text"].strip()
                        lower_text = text.lower()
                        
                        # Determine automated response
                        if lower_text.startswith("/start") or lower_text.startswith("/help"):
                            reply = (
                                f"🤖 *Welcome to {bot['name']}*\n\n"
                                f"_{bot['description']}_\n\n"
                                f"🚀 Access Portal: {bot['url']}\n"
                                f"📂 Central Hub: https://ram133.github.io/open-webui-cloud/\n\n"
                                f"*Commands:*\n"
                                f"• /portal - Get direct app link\n"
                                f"• /support - Get contact details\n"
                                f"• /price - View hourly service info"
                            )
                        elif lower_text.startswith("/portal"):
                            reply = f"👉 *Your Portal Link:* {bot['url']}"
                        elif lower_text.startswith("/support") or "support" in lower_text:
                            reply = "📞 *Support Contact:* crh2509@icloud.com | Signal: 671-456-6963"
                        elif lower_text.startswith("/price") or "price" in lower_text or "cost" in lower_text:
                            reply = "💳 *Hourly Services & Pricing:* https://www.ray.services/work/index.php"
                        elif any(kw in lower_text for kw in ["openwebui", "texcool", "ray2fb", "0724", "cloud", "github", "deploy", "ai", "bot"]):
                            reply = f"🚀 *Automated Match!*\nExplore our platform: {bot['url']}\nSupport: crh2509@icloud.com"
                        else:
                            # Default engagement reply for any message
                            reply = f"Thanks for messaging {bot['name']}! Check out our live tools at {bot['url']} or type /help for options."
                            
                        success = send_message(token, chat_id, reply)
                        events.append({
                            "chat_id": chat_id,
                            "text": text,
                            "response_sent": success
                        })
    except Exception as e:
        print(f"Error handling {bot['name']}: {e}")
    return events

if __name__ == "__main__":
    print("Running Advanced Cloud Telegram Bot Daemon...")
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
