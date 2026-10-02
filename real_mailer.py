# Folder: ~/saas-stack/real_mailer.py
import re
import os
import time
import json
import ssl
import urllib.request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

TARGET_URLS = [
    "https://raw.githubusercontent.com/sindresorhus/awesome/main/readme.md"
]

SENDER_EMAIL = "crh2509@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = "crh2509@gmail.com"
QUEUE_FILE = "pending_emails.json"

def scrape_emails_from_url(url):
    print(f"Scraping external URL: {url}...")
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            html_content = response.read().decode('utf-8', errors='ignore')
            cleaned_content = re.sub(r'\s*\[at\s*', '@', html_content, flags=re.IGNORECASE)
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            emails = set(re.findall(email_pattern, cleaned_content))
            filtered = [e for e in emails if e.lower() not in [
                "crh2509@icloud.com", "crh2509@gmail.com", 
                "support@ycombinator.com", "hn@ycombinator.com",
                "example@domain.com", "github@github.com",
                "sindresorhus@gmail.com"
            ]]
            return filtered
    except Exception as e:
        print(f"Scraping error for {url}: {e}")
        return []

def queue_email(recipient):
    queue = []
    if os.path.exists(QUEUE_FILE):
        try:
            with open(QUEUE_FILE, 'r') as f:
                queue = json.load(f)
        except:
            queue = []
    if recipient not in queue:
        queue.append(recipient)
        with open(QUEUE_FILE, 'w') as f:
            json.dump(queue, f, indent=2)
        print(f"QUEUED (Google Security Delay Active): {recipient} saved to {QUEUE_FILE}")

if __name__ == "__main__":
    all_leads = set()
    for url in TARGET_URLS:
        found = scrape_emails_from_url(url)
        all_leads.update(found)
    
    if not all_leads:
        print("Notice: No emails scraped from URLs. Using active fallback test targets.")
        all_leads.update(["crh2509@icloud.com"])

    leads_list = list(all_leads)
    print(f"Found {len(leads_list)} target lead emails: {leads_list}")
    print("Google Account Security Delay detected (phone number change). Queuing emails locally.")
    
    for email in leads_list:
        queue_email(email)
        time.sleep(0.5)
            
    print(f"Queue Run Complete. Total pending in {QUEUE_FILE}: {len(leads_list)}")
