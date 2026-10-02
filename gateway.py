import http.server
import socketserver
import json
import os

PORT = 8787
LEDGER_PATH = os.path.expanduser("~/saas-stack/data/ledger.json")

class GatewayHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data.decode('utf-8'))
            
            os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)
            ledger = {"total_revenue_coins": 0, "transactions": []}
            if os.path.exists(LEDGER_PATH):
                with open(LEDGER_PATH, "r") as f:
                    ledger = json.load(f)
            
            price_str = data.get("price", "0").split()[0]
            price_val = int(price_str) if price_str.isdigit() else 10
            
            ledger["total_revenue_coins"] += price_val
            ledger["transactions"].append(data)
            
            with open(LEDGER_PATH, "w") as f:
                json.dump(ledger, f, indent=4)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "coins_earned": price_val}).encode('utf-8'))
            print(f"💰 [RayGateway] Earned {price_val} 671-Coins from {data.get('item', 'Service')}!")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Typehttps://ram133.github.io/open-webui-cloud/

### What this does:
This script creates and launches the local HTTP transaction gateway daemon (`gateway.py`) running on port 8787. It automatically captures incoming orders and micro-tool payments from your decentralized tools, updates your local revenue ledger (`ledger.json`), and records every 671-Coin transaction in real time.

---

### Folder Path & File Name: `~/saas-stack/gateway.py`
Run this clean block in your terminal to deploy and start the local transaction server:

```bash
cat << 'EOF' > ~/saas-stack/gateway.py
import http.server
import socketserver
import json
import os

PORT = 8787
LEDGER_PATH = os.path.expanduser("~/saas-stack/data/ledger.json")

class GatewayHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data.decode('utf-8'))
            os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)
            
            if os.path.exists(LEDGER_PATH):
                with open(LEDGER_PATH, "r") as f:
                    ledger = json.load(f)
            else:
                ledger = {"total_revenue_coins": 0, "transactions": []}
            
            ledger["transactions"].append(data)
            # Simple coin accumulator parser
            price_str = data.get("price", "0")
            coins = int(''.join(filter(str.isdigit, price_str)) or 0)
            ledger["total_revenue_coins"] += coins
            
            with open(LEDGER_PATH, "w") as f:
                json.dump(ledger, f, indent=4)
                
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "logged": data}).encode('utf-8'))
            print(f"💰 [RayGateway] Autonomous Transaction Logged: {data.get('item')} | Revenue: +{coins} Coins")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            print(f"⚠️ Gateway Error: {e}")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

with socketserver.TCPServer(("", PORT), GatewayHandler) as httpd:
    print(f"⚡ [RayGateway] Active on port {PORT}. Listening for 671-Coin transactions...")
    httpd.serve_forever()
