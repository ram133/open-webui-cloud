import http.server
import socketserver
import json
import os

PORT = 8787
LEDGER_PATH = os.path.expanduser("~/saas-stack/data/ledger.json")

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

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

with ReusableTCPServer(("", PORT), GatewayHandler) as httpd:
    print(f"⚡ [RayGateway] Active on port {PORT}. Listening for 671-Coin transactions...")
    httpd.serve_forever()
