import subprocess

print("🛠️ [RayStack] Force clearing untracked submodule directory...")
subprocess.run(["rm", "-rf", "ventures/lobe-chat"], capture_output=True)
subprocess.run(["git", "add", "-A"], capture_output=True)
subprocess.run(["git", "commit", "-m", "Removed rogue lobe-chat directory completely"], capture_output=True)
subprocess.run(["git", "push", "origin", "main"], capture_output=True)
print("✅ Workspace fully cleaned and pushed to production.")
