import os

HUB_DIR = os.path.expanduser("~/saas-stack/tools/hub")
os.makedirs(HUB_DIR, exist_ok=True)

master_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RayServices Master Micro-SaaS Hub</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; max-width: 900px; margin: 40px auto; padding: 20px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        h1 { color: #38bdf8; font-size: 2.2rem; text-align: center; margin-bottom: 5px; }
        .subtitle { text-align: center; color: #94a3b8; font-size: 1.1rem; margin-bottom: 30px; }
        .stats-bar { background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 15px; text-align: center; font-size: 1.1rem; margin-bottom: 30px; color: #38bdf8; font-weight: bold; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; }
        .card { background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 20px; transition: transform 0.2s, border-color 0.2s; display: flex; flex-direction: column; justify-content: space-between; }
        .card:hover { transform: translateY(-3px); border-color: #38bdf8; }
        .card h2 { color: #38bdf8; font-size: 1.25rem; margin-top: 0; }
        .card p { color: #cbd5e1; font-size: 0.95rem; flex-grow: 1; }
        .btn { display: inline-block; background: #0ea5e9; color: white; text-align: center; text-decoration: none; padding: 10px 16px; font-weight: bold; border-radius: 6px; margin-top: 15px; transition: background 0.2s; }
        .btn:hover { background: #0284c7; }
        .footer { text-align: center; margin-top: 40px; color: #64748b; font-size: 0.85rem; }
    </style>
</head>
<body>
    <h1>⚡ RayServices Master Hub</h1>
    <div class="subtitle">Decentralized 671-Coin Autonomous Micro-SaaS Ecosystem</div>
    
    <div class="stats-bar" id="statsBar">
        📊 Total Ecosystem Revenue: Loading Ledger...
    </div>
    
    <div class="grid">
        <div class="card">
            <div>
                <h2>AI Prompt Optimizer</h2>
                <p>Transform raw ideas and rough notes into high-performance, expert-level system prompts instantly.</p>
            </div>
            <a class="btn" href="http://localhost:8080" target="_blank">Launch Tool (671 Coins)</a>
        </div>
        
        <div class="card">
            <div>
                <h2>AI Code Generator</h2>
                <p>Generate clean, production-ready Python automation scripts with secure error handling.</p>
            </div>
            <a class="btn" href="http://localhost:8082" target="_blank">Launch Tool (671 Coins)</a>
        </div>
        
        <div class="card">
            <div>
                <h2>AI Text Summarizer</h2>
                <p>Condense lengthy articles and documents into concise executive bullet points.</p>
            </div>
            <a class="btn" href="http://localhost:8083" target="_blank">Launch Tool (671 Coins)</a>
        </div>
    </div>

    <div class="footer">
        Powered by RayNV Architecture &bull; Secured via RayGateway Port 8787
    </div>

    <script>
        async function fetchLedger() {
            try {
                const res = await fetch('http://localhost:8787/ledger');
                const data = await res.json();
                document.getElementById('statsBarinnerHTML = `📊 Total Ecosystem Revenue: ${data.total_revenue_coins} Coins (${data.transactions.length} Active Transactions)`;
            } catch (e) {
                // Fallback display if ledger endpoint is direct payload
                document.getElementById('statsBar').innerHTML = `📊 Ecosystem Active • Standard Pass Price: 671 Coins`;
            }
        }
        fetchLedger();
    </script>
</body>
</html>
"""

with open(os.path.join(HUB_DIR, "index.html"), "w") as f:
    f.write(master_html)

print("🚀 [RayStack] Master Hub deployed successfully at ~/saas-stack/tools/hub/index.html")
