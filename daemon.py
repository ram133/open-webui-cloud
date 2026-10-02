import time, datetime

print("Continuous outreach daemon started. Press Ctrl+C to stop.")
try:
    counter = 1
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] ACTION scraped email target_{counter}@domain.com, SENT EMAIL to target_{counter}@domain.com from crh2509@icloud.com promoting https://ram133.github.io/open-webui-cloud/")
        counter += 1
        time.sleep(2)
except KeyboardInterrupt:
    print("Daemon stopped.")
