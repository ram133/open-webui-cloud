# https://github.com/ram133/open-webui-cloud
import json
import os

LEDGER_FILE = "coins.json"

def init_ledger():
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, 'r') as f:
            return json.load(f)
    
    # Initialize airdrop for sample Guam numbers (671 prefix)
    ledger = {
        "token_name": "671-Coin",
        "total_supply": 1000000,
        "circulating": 0,
        "balances": {}
    }
    
    # Generate deterministic initial airdrop pool for 671 exchanges
    for i in range(1000, 1050):
        phone = f"+1671456{i}"
        ledger["balances"][phone] = 1000  # 1000 coins airdropped per number
        ledger["circulating"] += 1000

    save_ledger(ledger)
    return ledger

def save_ledger(data):
    with open(LEDGER_FILE, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    ledger = init_ledger()
    print(f"671-Coin Ledger Active. Total Supply: {ledger['total_supply']} | Circulating: {ledger['circulating']}")
    print(f"Registered Guam Numbers: {len(ledger['balances'])}")
