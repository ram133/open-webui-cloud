# https://github.com/ram133/open-webui-cloud
import urllib.request
import urllib.parse
import json
import time

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

def poll_bot(bot, offsets):
    token = bot["token"]
    offset = offsets.get(token, 0)
    url = f"https://api.telegram.org/bot{token}/getUpdates?offset={offset}&timeout=5"
    
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data.get("ok"):
                for result in data.get("result", []):
                    update_id = result["update_id"]
                    offsets[token] = update_id + 1
                    
                    msg = result.get("message") or result.get("edited_message")
                    if msg and "text" in msg and "chat" in msg:
                        chat_id = msg["chat"]["id"]
                        text = msg["text"].lower()
                        
                        if any(kw in text for kw in KEYWORDS):
                            print(f"[{bot['name']}] Keyword matched in chat {chat_id}: '{msg['text']}'")
                            send_message(token, chat_id, bot["response"])
    except Exception:
        pass

if __name__ == "__main__":
    print("Starting Continuous Telegram Bot Keyword Daemon...")
    offsets = {}
    
    while True:
        for bot in BOTS:
            poll_bot(bot, offsets)
        time.sleep(2)
