# https://github.com/ram133/open-webui-cloud
import json
import os
import subprocess
import time

LEDGER_FILE = "coins.json"

def send_imessage(phone, message):
    script = f'''
    tell application "Messages"
        set targetService to 1st account whose service type = iMessage
        set targetBuddy to participant "{phone}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''
    try:
        subprocess.run(['osascript', '-e', script], check=True)
        return True
    except Exception as e:
        print(f"Failed to send to {phone}: {e}")
        return False

def main():
    if not os.path.exists(LEDGER_FILE):
        print("No coins.json found.")
        return
    
    with open(LEDGER_FILE, 'r') as f:
        data = json.load(f)
    
    balances = data.get("balances", {})
    print(f"Starting iMessage outreach to {len(balances)} holders...")
    
    for phone in balances.keys():
        msg = "Hey! We are buying back 671-Coins to build market scarcity. What's your best offer?"
        print(f"Messaging {phone}...")
        success = send_imessage(phone, msg)
        if success:
            print(f"Offer sent to {phone}")
        time.sleep(15) # Steady pacing to prevent flooding

if __name__ == "__main__":
    main()
