import os

TOOL_DIR = os.path.expanduser("~/saas-stack/tools/optimizer")
os.makedirs(TOOL_DIR, exist_ok=True)

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>671-Coin AI Prompt Optimizer</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; max-width: 600px; margin: 40px auto; padding: 20px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        h1 { color: #38bdf8; font-size: 1.5rem; text-align: center; }
        textarea { width: 100%; height: 120px; background: #1e293b; color: #fff; border: 1px solid #334155; border-radius: 8px; padding: 12px; font-size: 1rem; box-sizing: border-box; resize: vertical; margin-bottom: 15px; }
        button { background: #0ea5e9; color: white; border: none; padding: 12px 20px; font-size: 1rem; font-weight: bold; border-radius: 8px; cursor: pointer; width: 100%; transition: background 0.2s; }
        button:hover { background: #0284c7; }
        #output { margin-top: 20px; background: #1e293b; padding: 15px; border-radius: 8px; border: 1px solid #334155; white-space: pre-wrap; display: none; }
    </style>
</head>
<body>
    <h1>⚡ 671-Coin AI Prompt Optimizer</h1>
    <p style="text-align: center; color: #94a3b8; font-size: 0.9rem;">Transform raw ideas into high-performance LLM system prompts.</p>
    
    <label for="rawPrompt">Enter Raw Prompt / Idea:</label>
    <textarea id="rawPrompt" placeholder="e.g. Write a python script to scrape a website..."></textarea>
    
    <button onclick="buyAndOptimize()">Optimize Prompt (Price: 671 Coins)</button>
    
    <div id="output"></div>

    <script>
        async function buyAndOptimize() {
            const raw = document.getElementById('rawPrompt').value;
            if(!raw) { alert('Please enter a prompt first.'); return; }

            const payload = {
                item: "AI Prompt Optimizer Pass",
                price: "671 Coins",
                customer: "client@" + window.location.hostname,
                input_data: raw
            };

            try {
                const res = await fetch('http://localhost:8787/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const data = await res.json();
                
                if(data.status === 'success') {
                    const out = document.getElementById('output');
                    out.style.display = 'block';
                    out.innerHTML = `<strong>✅ Payment Confirmed (${data.logged.price})!</strong><br><br><strong>Optimized Output:</strong><br>Act as an expert software engineer. Analyze the following requirement, structure the code robustly with error handling, and output clean modular syntax: "${raw}"`;
                } else {
                    alert('Gateway transaction failed.');
                }
            } catch (err) {
                alert('Could not connect to RayGateway on port 8787. Ensure gateway.py is running.');
            }
        }
    </script>
</body>
</html>
"""

with open(os.path.join(TOOL_DIR, "index.html"), "w") as f:
    f.write(html_content)

print("🚀 [RayStack] Prompt Optimizer Micro-Tool generated at ~/saas-stack/tools/optimizer/index.html")
