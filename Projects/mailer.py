import json
import smtplib
import ssl
from email.message import EmailMessage
import os

# Your email credentials
SENDER_EMAIL = ""
SENDER_PASSWORD = ""

# Load participant data
with open("data_with_certificates.json") as f:
    participants = json.load(f)

# SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Email content
SUBJECT = "Your Participation Certificate"
BODY_TEMPLATE = """\
Dear {name},

Thank you for participating in our event. Please find your certificate attached.

Best regards,
The Organizing Team
"""

# Send emails
context = ssl.create_default_context()

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls(context=context)
    server.login(SENDER_EMAIL, "lzmn uwrt fvjt skvc")

    for person in participants[0:5]:
        name = person["name"]
        email = person["email"]
        cert_path = person["certificate"]

        if not os.path.exists(cert_path):
            print(f"Certificate not found for {name}, skipping.")
            continue

        msg = EmailMessage()
        msg["From"] = SENDER_EMAIL
        msg["To"] = "bibekjoshi34@gmail.com"  # ← use the actual recipient
        msg["Subject"] = SUBJECT
        msg.set_content(BODY_TEMPLATE.format(name=name))

        with open(cert_path, "rb") as cert_file:
            cert_data = cert_file.read()
            cert_name = os.path.basename(cert_path)
            msg.add_attachment(
                cert_data, maintype="image", subtype="jpeg", filename=cert_name
            )

        try:
            server.send_message(msg)
            print(f"✅ Email sent to {name} ({email})")
        except Exception as e:
            print(f"❌ Failed to send email to {name} ({email}): {e}")
