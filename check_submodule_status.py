import subprocess

print("🔍 [RayStack] Checking Git submodule status...")
result = subprocess.run(["git", "submodule", "status"], capture_output=True, text=True)
print(result.stdout if result.stdout else "No submodule output detected.")
