import os
import subprocess

# Kill any existing process on port 8787
os.system("lsof -ti :8787 | xargs kill -9 2>/dev/null")

# Start gateway in background
subprocess.Popen(["python3", os.path.expanduser("~/saas-stack/gateway.py")])
print("🚀 [RayStack] RayGateway successfully restarted on port 8787!")
