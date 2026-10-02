import time
import subprocess
import os

os.chdir(os.path.expanduser("~/saas-stack"))
print("⚡ [RayPulse] Autonomous Git Watcher Active...")

while True:
    try:
        # Check for local changes
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status.stdout.strip():
            print("⚡ Changes detected. Auto-syncing ecosystem...")
            subprocess.run(["git", "add", "."])
            subprocess.run(["git", "commit", "-m", "Auto-sync: RayPulse autonomous background update"])
            subprocess.run(["git", "pull", "origin", "main", "--rebase"])
            subprocess.run(["git", "push", "origin", "main"])
            print("✅ Ecosystem successfully synced to GitHub.")
    except Exception as e:
        print(f"⚠️ Watcher error: {e}")
    
    time.sleep(30)
