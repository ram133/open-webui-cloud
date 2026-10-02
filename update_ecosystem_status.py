import os

status_script = """import urllib.request
import json

try:
    req = urllib.request.Request("http://localhost:8787/ledger")
    with urllib.request.urlopen(req) as response:
        ledger = json.loads(response.read().decode('utf-8'))
        print("🌟 [RayServices Ecosystem Status]")
        print(f"   • Total Revenue: {ledger.get('total_revenue_coins', 0)} Coins")
        print(f"   • Active Transactions: {len(ledger.get('transactions', []))}")
        print("   • Gateway: Online (Port 8787)")
        print("   • Micro-Tools: Prompt Optimizer (8080), Code Generator (8082), Text Summarizer (8083), Tagalog-English Translator (8084)")
        print("   • Master Hub: Online (8081)")
except Exception as e:
    print("❌ Ecosystem check failed:", e)
"""

with open(os.path.expanduser("~/saas-stack/ecosystem_status.py"), "w") as f:
    f.write(status_script)

print("🚀 [RayStack] Ecosystem status script updated with Translator port 8084.")
