import subprocess

print("🧹 [RayStack] Completely removing and cleaning dirty submodule reference...")
subprocess.run(["git", "rm", "-f", "ventures/lobe-chat"], capture_output=True)
subprocess.run(["rm", "-rf", ".git/modules/ventures/lobe-chat"], capture_output=True)
subprocess.run(["git", "add", "."], capture_output=True)
subprocess.run(["git", "commit", "-m", "Completely removed dirty lobe-chat submodule"], capture_output=True)
print("✅ Submodule completely excised and repository tree normalized.")
