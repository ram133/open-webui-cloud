# https://github.com/ram133/open-webui-cloud
import urllib.request
import urllib.parse
import json
import time
import os

BOT_CONFIGS = [
    {
        "token": "7464269358:AAEcUuwyX77QOAh6i_NJyPcYfNfhLreu3Lw",
        "name": "TEXCOOLBot",
        "url": "https://ray2407.github.io/texcool"
    },
    {
        "token": "8056349243:AAH7CVgBx5_ese73xjCg3ah71T6-NlrOeaI",
        "name": "Ray2FB Bot",
        "url": "https://ray2407.github.io/ray2fb"
    },
    {
        "token": "7355656881:AAEe3hHYjDAlg6aVQ8Iw8M125qxqBxlnYK4",
        "name": "0724 Bot",
        "url": "https://ray2407.github.io/0724"
    },
    {
        "token": "7942570289:AAGYVe68mlMo14qXfDLEXhDInOhAcnVvhPA",
        "name": "RayoR (@CRH2511Bot)",
        "url": "https://ram133.github.io/open-webui-cloud/"
    }
]

CONFIG_FILE = "broadcast.json"

def load_targets(token):
    targets = set()
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                data = json.load(f)
                targets.update(data.get("channels", []))
                targets.update(data.get("chat_ids", []))
        except Exception:
            pass

    url = f"https://api.telegram.org/bot{token}/getUpdates"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            if data.get("ok"):
                for result in data.get("result", []):
                    message = result.get("message") or result.get("edited_message") or result.get("channel_post")
                    if message and "chat" in message:
                        targets.add(message["chat"]["id"])
    except Exception as e:
        print(f"Notice: getUpdates warning for bot: {e}")
        
    return list(targets)

def send_telegram_message(token, chat_target, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode({
        "chat_id": chat_target,
        "text": text,
        "parse_mode": "Markdown"
    }).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=payload, method="POST")
        with urllib.request.urlopen(req, timeout=10) as response:
            res = json.loads(response.read().decode('utf-8'))
            return res.get("ok", False), ""
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8', errors='ignore')
        return False, f"HTTP Error {e.code}: {error_body}"
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    print("Initializing Expanded Branded Multi-Bot Telegram Marketing Pipeline...")
    total_sent = 0
    
    for bot in BOT_CONFIGS:
        token = bot["token"]
        bot_name = bot["name"]
        target_url = bot["url"]
        
        message = (
            f"🚀 *Explore {bot_name} Portal*\n\n"
            f"Access live decentralized web applications:\n"
            f"👉 {target_url}\n\n"
            f"Central Cloud Hub: https://ram133.github.io/open-webui-cloud/\n"
            f"Support: crh2509@icloud.com | Signal: 671-456-6963"
        )
        
        print(f"\n[{bot_name}] Resolving target chats/channels...")
        targets = load_targets(token)
        if not targets:
            print(f"[{bot_name}] No targets found. Skipping.")
            continue
            
        print(f"[{bot_name}] Found {len(targets)} target(s). Broadcasting...")
        for target in targets:
            success, err_msg = send_telegram_message(token, target, message)
            if success:
                print(f"  -> SUCCESS: Sent via {bot_name} to {target}")
                total_sent += 1
            else:
                print(f"  -> ERROR: Failed sending via {bot_name} to {target} | {err_msg}")
            time.sleep(0.5)
            
    print(f"\nBroadcast Complete. Total messages delivered: {total_sent}")
