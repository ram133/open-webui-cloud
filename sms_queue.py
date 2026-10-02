# Folder: ~/saas-stack/sms_queue.py
import json
import os

PHONE_QUEUE_FILE = "local_phone_leads.json"

DEFAULT_LOCAL_NUMBERS = [
    "+16714566963",
    "+16715550199",
    "+16715550142"
]

def initialize_phone_queue():
    if not os.path.exists(PHONE_QUEUE_FILE):
        with open(PHONE_QUEUE_FILE, 'w') as f:
            json.dump(DEFAULT_LOCAL_NUMBERS, f, indent=2)
        print(f"Initialized {PHONE_QUEUE_FILE} with default Guam numbers.")

def load_phone_queue():
    initialize_phone_queue()
    with open(PHONE_QUEUE_FILE, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    phones = load_phone_queue()
    print(f"Loaded {len(phones)} local phone leads from queue:")
    for phone in phones:
        print(f" - Target: {phone} | Message: Deploy Open WebUI Cloud | Support: 671-456-6963")
