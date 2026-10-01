# https://github.com/ram133/open-webui-cloud
import json
import os

LEDGER_FILE = "guam_coins.json"
MY_PHONE = "+16714566963"

def inject_personal_ping():
    if not os.path.exists(LEDGER_FILE):
        return
    
    with open(LEDGER_FILE, 'r') as f:
        data = json.load(f)
        
    # Ensure personal number is credited and forced back to pending for hourly live testing
    data["balances"][MY_PHONE] = 100
    data["outreach_status"][MY_PHONE] = "pending"
    
    with open(LEDGER_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Injected personal number {MY_PHONE} into active airdrop & outreach queue.")

if __name__ == "__main__":
    inject_personal_ping()
