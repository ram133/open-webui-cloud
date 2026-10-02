import urllib.request
import json

url = "http://localhost:8787/"
payload = {
    "item": "AI Productivity Suite Pass",
    "price": "671 Coins",
    "customer": "test_client@ray.services"
}

req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST'
)

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        print("✅ Payment Gateway Response:", json.dumps(result, indent=2))
except Exception as e:
    print("❌ Error connecting to RayGateway:", e)
