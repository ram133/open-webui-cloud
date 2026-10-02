import urllib.request
import json

try:
    req = urllib.request.Request("http://localhost:8787/ledger")
    with urllib.request.urlopen(req) as response:
        ledger = json.loads(response.read().decode('utf-8'))
        print("✅ [RayGateway] /ledger endpoint verified successfully:")
        print(json.dumps(ledger, indent=2))
except Exception as e:
    print("❌ Error reaching /ledger endpoint:", e)
