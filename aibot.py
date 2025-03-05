from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr
import random
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Store email and OTPs in memory (for production, use a database)
otp_storage = {}

class EmailRequest(BaseModel):
    email: EmailStr

class OTPRequest(BaseModel):
    email: EmailStr
    otp: str

# Function to send OTP
def send_otp_email(email, otp):
    sender_email = os.getenv("EMAIL_SENDER")
    sender_password = os.getenv("EMAIL_PASSWORD")
    
    msg = EmailMessage()
    msg.set_content(f"Your OTP code is: {otp}")
    msg["Subject"] = "Your Verification Code"
    msg["From"] = sender_email
    msg["To"] = email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to send email.")

# Endpoint to request OTP
@app.post("/send-otp/")
def send_otp(request: EmailRequest):
    otp = str(random.randint(100000, 999999))
    otp_storage[request.email] = otp
    send_otp_email(request.email, otp)
    return {"message": "OTP sent to email."}

# Endpoint to verify OTP
@app.post("/verify-otp/")
def verify_otp(request: OTPRequest):
    if request.email in otp_storage and otp_storage[request.email] == request.otp:
        del otp_storage[request.email]
        return {"message": "OTP verified successfully."}
    else:
        raise HTTPException(status_code=400, detail="Invalid OTP.")
