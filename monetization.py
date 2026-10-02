import os
import json

LEDGER_PATH = os.path.expanduser("~/saas-stack/data/ledger.json")
os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)

if not os.path.exists(LEDGER_PATH):
    with open(LEDGER_PATH, "w") as f:
        json.dump({"total_revenue_coins": 0, "transactions": []}, f, indent=4)

print("⚡ [RayPulse] Ledger initialized. Autonomous monetization loops armed.")
