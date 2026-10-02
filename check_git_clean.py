import subprocess

print("🔍 [RayStack] Verifying clean Git working tree status...")
result = subprocess.run(["git", "status"], capture_output=True, text=True)
print(result.stdout)
