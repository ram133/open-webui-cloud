import os

WORKSPACE = os.path.expanduser("~/saas-stack/ventures")
dashboard_path = os.path.expanduser("~/saas-stack/index.html")

ventures = [d for d in os.listdir(WORKSPACE) if os.path.isdir(os.path.join(WORKSPACE, d))]

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RayNV | Autonomous Ventures Hub</title>
    <style>
        body {{ background: #0f172a; color: #f8fafc; font-family: -apple-system, sans-serif; padding: 40px; margin: 0; }}
        h1 {{ color: #38bdf8; font-size: 2rem; margin-bottom: 10px; }}
        p {{ color: #94a3b8; margin-bottom: 30px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }}
        .card {{ background: #1e293b; border: 1px solid #334155; padding: 24px; border-radius: 12px; transition: 0.2s; }}
        .card:hover {{ border-color: #38bdf8; transform: translateY(-2px); }}
        h3 {{ margin-top: 0; color: #f1f5f9; text-transform: capitalize; }}
        a {{ display: inline-block; background: #0284c7; color: white; padding: 10px 16px; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 15px; }}
        a:hover {{ background: #0369a1; }}
    </style>
</head>
<body>
    <h1>⚡ RayNV Autonomous Ventures</h1>
    <p>Live decentralized income-generating nodes powered by 671-Coin architecture.</p>
    <div class="grid">
"""

for v in ventures:
    html_content += f"""
        <div class="card">
            <h3>{v.replace('-', ' ')}</h3>
            <p>Monetized micro-SaaS instance running locally on RayPulse engine.</p>
            <a href="./ventures/{v}/index.html" target="_blank">Launch Venture →</a>
        </div>
    """

html_content += """
    </div>
</body>
</html>
"""

with open(dashboard_path, "w") as f:
    f.write(html_content)

print(f"✅ Autonomous Ventures Dashboard generated at {dashboard_path}")
