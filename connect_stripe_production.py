import json
import os

config_path = os.path.expanduser("~/saas-stack/gateway_config.json")

config = {
    "mode": "production",
    "gateway_port": 8787,
    "currency": "671-Coin / USD",
    "stripe_integration": "active",
    "paypal_email": "crh2509@icloud.com",
    "public_endpoints": [
        "https://ram133.github.io/open-webui-cloud/"
    ]
}

with open(config_path, "w") as f:
    json.dump(config, f, indent=2)

print("💳 [RayStack] Stripe and live production gateway configuration successfully updated.")
print("🌐 Destination Email set to: crh2509@icloud.com")
