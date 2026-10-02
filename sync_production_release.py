import subprocess

print("🚀 [RayStack] Publishing latest local commits to origin/main...")
result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
print(result.stdout if result.stdout else result.stderr)
print("✅ Production branch fully synchronized with remote.")
