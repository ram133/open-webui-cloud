# https://github.com/ram133/open-webui-cloud
import json
import os
import subprocess
import time

LEDGER_FILE = "guam_coins.json"
MY_PHONE = "+16714566963"

def send_imessage(phone, message):
    script = f'''
    tell application "Messages"
        set targetService to 1st account whose service type = iMessage
        set targetBuddy to participant "{phone}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''
    try:
        subprocess.run(['osascript', '-e', script], check=True, timeout=10)
        return True
    except Exception:
        return False

def run_batch():
    if not os.path.exists(LEDGER_FILE):
        print("Run guam_airdrop.py first.")
        return
        
    with open(LEDGER_FILE, 'r') as f:
        data = json.load(f)
        
    balances = data["balances"]
    status = data["outreach_status"]
    
    count = 0
    
    # Priority check: Always send to your personal number first on every run for live verification
    if MY_PHONE in status:
        msg = f"Hafa Adai! [Live System Ping] You've been airdropped 100 eco-coins to your Guam number ({MY_PHONE}). We're building local scarcity and buying back tokens. What is your best offer?"
        print(f"Sending priority live verification ping to {MY_PHONE}...")
        if send_imessage(MY_PHONE, msg):
            status[MY_PHONE] = "sent"
            count += 1
            time.sleep(5)
            
    # Then proceed with regular batch pagination for other numbers
    for phone, state in status.items():
        if phone == MY_PHONE:
            continue
        if state == "pending" and count < 50:
            msg = f"Hafa Adai! You've been airdropped 100 eco-coins to your Guam number ({phone}). We're building local scarcity and buying back tokens. What is your best offer?"
            print(f"Sending natural outreach to {phone}...")
            
            if send_imessage(phone, msg):
                status[phone] = "sent"
                count += 1
                time.sleep(20)
            else:
                status[phone] = "failed"
                
    with open(LEDGER_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Batch complete. Processed {count} messages.")

if __name__ == "__main__":
    run_batch()
