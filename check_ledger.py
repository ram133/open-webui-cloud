import json
import os

LEDGER_PATH = os.path.expanduser("~/saas-stack/data/ledger.json")

if os.path.exists(LEDGER_PATH):
    with open(LEDGER_PATH, "r") as f:
        ledger = json.load(f)
    print("📊 [RayGateway] Current Ledger Status:")
    print(json.dumps(ledger, indent=4))
else:
    print("⚠️ Ledger file not found yet. Run a payment test first!")
