import os

TOOLS = [
    {"name": "ai-refactor", "title": "AI Code Refactor Engine", "desc": "Instantly optimize and clean production code snippets."},
    {"name": "seo-audit", "title": "Instant SEO & Metadata Audit", "desc": "Automated landing page audit for maximum search visibility."},
    {"name": "consulting-portal", "title": "1-on-1 Micro-Consulting Slot", "desc": "Book direct development and architecture advisory sessions."}
]

WORKSPACE = os.path.expanduser("~/saas-stack/ventures")
os.makedirs(WORKSPACE, exist_ok=True)

print("⚡ [RayPulse] Building autonomous micro-ecosystem tools...")

for tool in TOOLS:
    tool_dir = os.path.join(WORKSPACE, tool["name"])
    os.makedirs(tool_dir, exist_ok=True)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RayNV | {tool["title"]}</title>
    <style>
        body {{ background: #0f172a; color: #f8fafc; font-family: -apple-system, sans-serif; padding: 40px; max-width: 600px; margin: auto; }}
        h1 {{ color: #38bdf8; font-size: 1.8rem; }}
        input, textarea {{ width: 100%; padding: 12px; margin: 10px 0; background: #1e293b; border: 1px solid #334155; color: white; border-radius: 6px; box-sizing: border-box; }}
        button {{ background: #0284c7; color: white; border: none; padding: 12px 20px; border-radius: 6px; font-weight: bold; cursor: pointer; width: 100%; }}
        button:hover {{ background: #0369a1; }}
        #result {{ margin-top: 20px; background: #1e293b; padding: 15px; border-radius: 6px; display: none; }}
        a {{ color: #38bdf8; text-decoration: none; display: inline-block; margin-bottom: 20px; }}
    </style>
</head>
<body>
    <a href="../../index.html">← Back to Ventures Hub</a>
    <h1>⚡ {tool["title"]}</h1>
    <p>{tool["desc"]}</p>
    <form id="toolForm">
        <input type="text" id="name" placeholder="Your Name or Project" required>
        <input type="email" id="email" placeholder="Your Contact Email" required>
        <textarea id="inputData" rows="4" placeholder="Enter target data, code snippet, or requirements..." required></textarea>
        <button type="submit">Execute Autonomous Task (15 671-Coins)</button>
    </form>
    <div id="result"></div>
    <script>
        document.getElementById('toolForm').addEventListener('submit', async (e) => {{
            e.preventDefault();
            const payload = {{
                item: "{tool["title"]}",
                price: "15 671-Coins",
                buyer: document.getElementById('email').value,
                data: document.getElementById('inputData').value
            }};
            try {{
                const res = await fetch('http://localhost:8787/', {{
                    method: 'POST',
                    headers: {{ 'Content-Type': 'application/json' }},
                    body: JSON.stringify(payload)
                }});
                const resultDiv = document.getElementById('result');
                resultDiv.style.display = 'block';
                resultDiv.innerHTML = `<strong>✅ Transaction & Task Logged!</strong><br>Successfully routed to local RayGateway ledger.`;
            }} catch(err) {{
                alert('Gateway offline. Ensure local daemon is running on port 8787.');
            }}
        });
    </script>
</body>
</html>
"""
    with open(os.path.join(tool_dir, "index.html"), "w") as f:
        f.write(html)
    print(f"✅ Deployed: {tool['name']}")

print("⚡ Ecosystem Expansion Complete.")
