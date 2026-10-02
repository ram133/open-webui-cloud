import os
import subprocess

os.system("lsof -ti :8085 | xargs kill -9 2>/dev/null")
subprocess.Popen(["python3", "-m", "http.server", "8085", "--directory", os.path.expanduser("~/saas-stack/tools/reviewer")])
print("🚀 [RayStack] AI Code Reviewer successfully started on port 8085!")
