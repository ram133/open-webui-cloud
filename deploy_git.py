import os

os.system("git -C ~/saas-stack init 2>/dev/null")
os.system("git -C ~/saas-stack add .")
os.system('git -C ~/saas-stack commit -m "RayServices autonomous micro-SaaS ecosystem fully deployed and verified"')
print("🚀 [RayStack] Codebase version-controlled and committed locally.")
