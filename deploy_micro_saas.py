import os

HUB_DIR = os.path.expanduser("~/saas-stack/tools/hub")
os.makedirs(HUB_DIR, exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RayServices Micro-SaaS Hub</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; max-width: 800px; margin: 40px auto; padding: 20px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        h1 { color: #38bdf8; font-size: 2rem; text-align: center; }
        .subtitle { text-align: center; color: #94a3b8; font-size: 1rem; margin-bottom: 30px; }
        .grid { display: grid; grid-template-columns: 1fr; gap: 20px; }
        .card { background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 20px; transition: transform 0.2s; }
        .card:hover { transform: translateY(-3px); border-color: #38bdf8; }
        .card h2 { color: #38bdf8; font-size: 1.25rem; margin-top: 0; }
        .card p { color: #cbd5e1; font-size: 0.95rem; }
        .btn { display: inline-block; background: #0ea5e9; color: white; text-decoration: none; padding: 10px 16px; font-weight: bold; border-radius: 6px; margin-top: 10px; transition: background 0.2s; }
        .btn:hover { background: #0284c7; }
    </style>
</head>
<body>
    <h1>⚡ RayServices Micro-SaaS Hub</h1>
    <div class="subtitle">Decentralized 671-Coin Autonomous Micro-Tools</div>
    
    <div class="grid">
        <div class="card">
            <h2>AI Prompt Optimizer</h2>
            <p>Transform raw ideas and rough notes into high-performance, expert-level system prompts instantly.</p>
            <a class="btn" href="http://localhost:8080" target="_blank">Launch Tool (671 Coins)</a>
        </div>
    </div>
</body>
</html>
"""

with open(os.path.join(HUB_DIR, "index.html"), "w") as f:
    f.write(html_content)

print("🚀 [RayStack] Master Hub generated at ~/saas-stack/tools/hub/index.html")
