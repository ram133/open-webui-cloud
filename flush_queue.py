# Folder: ~/saas-stack/flush_queue.py
import os
import time
import json
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "crh2509@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = "crh2509@gmail.com"
QUEUE_FILE = "pending_emails.json"

def send_email(recipient, smtp_pass):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient
    msg['Subject'] = "Open WebUI Cloud Access & Deployment"
    
    body = "Hello,\n\nDeploy your dedicated Open WebUI instance instantly.\nAccess the payment portal: https://ram133.github.io/open-webui-cloud/\n\nSupport: crh2509@icloud.com | Signal: 671-456-6963"
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        print(f"Connecting to Gmail SMTP (SSL Port 465) for {recipient}...")
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context, timeout=20) as server:
            server.login(SMTP_USER, smtp_pass)
            server.send_message(msg)
        print(f"SUCCESS: Email sent to {recipient}")
        return True
    except Exception as e:
        print(f"SMTP Delivery Error for {recipient}: {e}")
        return False

if __name__ == "__main__":
    if not os.path.exists(QUEUE_FILE):
        print("No pending queue file found.")
        exit(0)
        
    with open(QUEUE_FILE, 'r') as f:
        queue = json.load(f)
        
    if not queue:
        print("Queue is empty.")
        exit(0)
        
    print(f"Loaded {len(queue)} pending emails from {QUEUE_FILE}.")
    app_password = input("Enter your 16-character Google App Password: ").strip()
    
    if not app_password:
        print("Aborted: App password required to flush queue.")
        exit(1)
        
    remaining = []
    success_count = 0
    
    for email in queue:
        if send_email(email, app_password):
            success_count += 1
        else:
            remaining.append(email)
        time.sleep(1)
        
    with open(QUEUE_FILE, 'w') as f:
        json.dump(remaining, f, indent=2)
        
    print(f"Queue Flush Complete. Sent: {success_count}, Remaining in queue: {len(remaining)}")
