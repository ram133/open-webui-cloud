import urllib.request
import json

url = "http://localhost:8787/"
payload = {
    "item": "Code Generator Pass",
    "price": "671 Coins",
    "customer": "coder_client@ray.services",
    "input_data": "Write a script to monitor disk space"
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
        print("✅ Code Generator Payment Response:", json.dumps(result, indent=2))
except Exception as e:
    print("❌ Error connecting to RayGateway:", e)
