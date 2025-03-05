import os
import random
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

# Store OTPs
otp_storage = {}

def send_otp(email):
    otp = str(random.randint(100000, 999999))
    otp_storage[email] = otp
    send_email(email, otp)
    return {"message": "OTP sent to email."}

def verify_otp(email, otp):
    if email in otp_storage and otp_storage[email] == otp:
        del otp_storage[email]
        return {"message": "OTP verified successfully."}
    return {"error": "Invalid OTP"}

def send_email(receiver_email, otp):
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")

    msg = EmailMessage()
    msg.set_content(f"Your OTP code is: {otp}")
    msg["Subject"] = "Your Verification Code"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")
