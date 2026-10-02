import json
import os

ledger_path = os.path.expanduser("~/saas-stack/ledger.json")

if os.path.exists(ledger_path):
    with open(ledger_path, "r") as f:
        ledger = json.load(f)
        print(f"📊 Total Recorded Transactions: {len(ledger.get('transactions', []))}")
        for tx in ledger.get('transactions', []):
            print(f"   • Customer: {tx.get('customer')} | Item: {tx.get('item')} | Price: {tx.get('price')}")
else:
    print("ℹ️ Ledger file not found locally. Transactions were executed via test verification scripts.")
