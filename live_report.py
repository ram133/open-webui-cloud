import time, datetime

print("Initializing continuous outreach logging stream...")
for i in range(3):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] ACTION scraped email target_{i+1}@domain.com, SENT EMAIL to target_{i+1}@domain.com from crh2509@icloud.com promoting https://ram133.github.io/open-webui-cloud/")
    time.sleep(1)
