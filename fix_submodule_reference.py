import subprocess

print("🛠️ [RayStack] Fixing lobe-chat submodule reference...")
subprocess.run(["git", "config", "--file", ".gitmodules", "submodule.ventures/lobe-chat.ignore", "all"], capture_output=True)
subprocess.run(["git", "add", ".gitmodules"], capture_output=True)
subprocess.run(["git", "commit", "-m", "Ignored dirty status on lobe-chat submodule"], capture_output=True)
print("✅ Submodule reference updated and locked.")
