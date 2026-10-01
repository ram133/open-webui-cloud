# https://github.com/ram133/open-webui-cloud
import json
import os
import random

LEDGER_FILE = "guam_coins.json"

def generate_guam_ledger():
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, 'r') as f:
            return json.load(f)
    
    # Common Guam mobile and landline exchange prefixes (Docomo, GTA, IT&E)
    exchanges = ["482", "483", "688", "333", "644", "922", "727", "898", "477", "475"]
    
    ledger = {
        "token_name": "Guam-Coin",
        "total_supply": 7000000,
        "balances": {},
        "outreach_status": {}
    }
    
    print("Generating airdrop ledger for 70,000+ Guam numbers...")
    
    # Generate structured base for over 70,000 unique numbers
    for ex in exchanges:
        for i in range(10000): # 10,000 per exchange block
            phone = f"+1671{ex}{i:04d}"
            ledger["balances"][phone] = 100
            ledger["outreach_status"][phone] = "pending"

    with open(LEDGER_FILE, 'w') as f:
        json.dump(ledger, f)
        
    print(f"Ledger initialized with {len(ledger['balances'])} accounts credited with 100 coins each.")
    return ledger

if __name__ == "__main__":
    generate_guam_ledger()
