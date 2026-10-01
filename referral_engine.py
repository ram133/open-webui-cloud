# https://github.com/ram133/open-webui-cloud
import json
import os

LEDGER_FILE = "guam_coins.json"

def process_referral(referrer_phone, new_phone):
    if not os.path.exists(LEDGER_FILE):
        return
    
    with open(LEDGER_FILE, 'r') as f:
        data = json.load(f)
        
    balances = data["balances"]
    
    if referrer_phone in balances and new_phone in balances:
        # Reward referrer with 50 coins, new user with bonus 50 coins (total 150)
        balances[referrer_phone] += 50
        balances[new_phone] += 50
        print(f"Viral referral credited: {referrer_phone} earned 50 coins for bringing in {new_phone}.")
        
    with open(LEDGER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    print("Referral engine active.")
