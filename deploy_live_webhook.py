import json
import os

webhook_path = os.path.expanduser("~/saas-stack/webhook_listener.py")

script_content = '''import http.server
import socketserver
import json
import os

PORT = 8788
LEDGER_PATH = os.path.expanduser("~/saas-stack/ledger.json")

class StripeWebhookHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            event = json.loads(post_data.decode('utf-8'))
            print(f"💰 [Live Webhook] Received Stripe Event: {event.get('type')}")
            
            # Log real transaction to ledger
            if os.path.exists(LEDGER_PATH):
                with open(LEDGER_PATH, "r") as f:
                    ledger = json.load(f)
            else:
                ledger = {"total_revenue_coins": 0, "transactions": []}
                
            new_tx = {
                "item": "Live Micro-Tool Pass",
                "price": "671 Coins",
                "customer": event.get("customer_email", "live_customer@ray.services")
            }
            ledger["transactions"].append(new_tx)
            ledger["total_revenue_coins"] += 671
            
            with open(LEDGER_PATH, "w") as f:
                json.dump(ledger, f, indent=2)
                
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'{"status": "success"}')
        except Exception as e:
            print(f"❌ Webhook Error: {e}")
            self.send_response(400)
            self.end_headers()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), StripeWebhookHandler) as httpd:
        print(f"🌐 [RayStack] Live Stripe Webhook Listener active on port {PORT}")
        httpd.serve_forever()
'''

with open(webhook_path, "w") as f:
    f.write(script_content)

print("🚀 [RayStack] Live Stripe webhook listener script successfully created.")
