import http.server
import json
import os
from datetime import datetime

PORT = 8787
LEDGER_PATH = os.path.expanduser("~/saas-stack/data/ledger.json")
os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)

class GatewayHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data.decode('utf-8'))
            record = {
                "timestamp": datetime.now().isoformat(),
                "item": data.get("item", "Unknown"),
                "price": data.get("price", "0 671-Coins"),
                "buyer": data.get("buyer", "Anonymous")
            }
            
            ledger = []
            if os.path.exists(LEDGER_PATH):
                with open(LEDGER_PATH, "r") as f:
                    try: ledger = json.load(f)
                    except: ledger = []
            ledger.append(record)
            with open(LEDGER_PATH, "w") as f:
                json.dump(ledger, f, indent=2)
                
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "logged": record}).encode())
            print(f"⚡ [Gateway] Order Logged: {record['item']} from {record['buyer']}")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == "__main__":
    print(f"⚡ RayGateway running locally on port {PORT}...")
    server = http.server.HTTPServer(('0.0.0.0', PORT), GatewayHandler)
    server.serve_forever()
