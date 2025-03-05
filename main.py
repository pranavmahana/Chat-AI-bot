from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from app.chatbot import chat_with_ai
from app.email_otp import send_otp, verify_otp

app = FastAPI()

# Chat API
class ChatRequest(BaseModel):
    message: str

@app.post("/chat/")
def chat(request: ChatRequest):
    response = chat_with_ai(request.message)
    return {"response": response}

# OTP APIs
class EmailRequest(BaseModel):
    email: EmailStr

@app.post("/send-otp/")
def request_otp(request: EmailRequest):
    return send_otp(request.email)

class OTPRequest(BaseModel):
    email: EmailStr
    otp: str

@app.post("/verify-otp/")
def validate_otp(request: OTPRequest):
    return verify_otp(request.email, request.otp)
