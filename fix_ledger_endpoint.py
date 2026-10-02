import os

GATEWAY_PATH = os.path.expanduser("~/saas-stack/gateway.py")

# Read existing gateway script if present, or write a complete one that includes the /ledger endpoint
gateway_code = """import http.server
import json
import os

PORT = 8787
LEDGER_FILE = os.path.expanduser("~/saas-stack/ledger.json")

def load_ledger():
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                pass
    return {"total_revenue_coins": 0, "transactions": []}

def save_ledger(ledger):
    with open(LEDGER_FILE, "w") as f:
        json.dump(ledger, f, indent=4)

class GatewayHandler(http.server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/ledger":
            ledger = load_ledger()
            response_data = json.dumps(ledger).encode('utf-8')
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(response_data)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            payload = json.loads(post_data.decode('utf-8'))
        except Exception as e:
            payload = {"error": "Invalid JSON"}

        ledger = load_ledger()
        price_str = payload.get("price", "671 Coins")
        try:
            coins = int(price_str.split()[0])
        except:
            coins = 671

        ledger["total_revenue_coins"] += coins
        ledger["transactions"].append(payload)
        save_ledger(ledger)

        response_payload = {
            "status": "success",
            "logged": payload,
            "total_revenue_coins": ledger["total_revenue_coins"]
        }
        
        response_data = json.dumps(response_payload).encode('utf-8')
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(response_data)

if __name__ == '__main__':
    server = http.server.HTTPServer(('0.0.0.0', PORT), GatewayHandler)
    print(f"🚀 [RayGateway] Running on port {PORT}...")
    server.serve_forever()
"""

with open(GATEWAY_PATH, "w") as f:
    f.write(gateway_code)

print("🚀 [RayStack] Gateway script updated with CORS and /ledger endpoint support.")
