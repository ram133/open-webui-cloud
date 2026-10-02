import os
import subprocess

TARGET_REPOS = [
    {"repo": "https://github.com/mckaywrigley/chatbot-ui", "name": "chatbot-ui"},
    {"repo": "https://github.com/lobehub/lobe-chat", "name": "lobe-chat"}
]

WORKSPACE = os.path.expanduser("~/saas-stack/ventures")
os.makedirs(WORKSPACE, exist_ok=True)

print("⚡ [RayPulse] Scanning with shallow clone optimization...")
for item in TARGET_REPOS:
    dest = os.path.join(WORKSPACE, item["name"])
    if not os.path.exists(dest):
        print(f"🚀 Shallow cloning asset: {item['name']}")
        subprocess.run(["git", "clone", "--depth", "1", item["repo"], dest])
        index_path = os.path.join(dest, "index.html")
        if os.path.exists(index_path):
            with open(index_path, "r") as f:
                content = f.read()
            monetized_content = content.replace("<body>", '<body>\n<script>console.log("⚡ 671-Coin Gateway Active");</script>')
            with open(index_path, "w") as f:
                f.write(monetized_content)
            print(f"✅ Repurposed {item['name']} with automated monetization layer.")
print("⚡ Autonomous Shallow Forking Complete.")
