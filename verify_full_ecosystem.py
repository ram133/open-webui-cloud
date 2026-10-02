import urllib.request
import json

print("🚀 [RayStack] Running complete ecosystem health and ledger audit...")

try:
    req = urllib.request.Request("http://localhost:8787/ledger")
    with urllib.request.urlopen(req) as response:
        ledger = json.loads(response.read().decode('utf-8'))
        print(f"📊 Ledger Status Verified:")
        print(f"   • Total Revenue: {ledger.get('total_revenue_coins', 0)} Coins")
        print(f"   • Total Transactions Logged: {len(ledger.get('transactions', []))}")
        for idx, tx in enumerate(ledger.get('transactions', []), 1):
            print(f"     [{idx}] {tx.get('item')} - {tx.get('price')} ({tx.get('customer')})")
except Exception as e:
    print("❌ Ledger audit failed:", e)

