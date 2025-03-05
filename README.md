# Chat-AI-bot
Historical AI Bot – FastAPI Chatbot with OTP Verification 🚀
This project is a FastAPI-based chatbot using LangGraph, LangChain, and OTP email verification. It can be deployed on Render and supports OpenAI GPT-based responses.

📌 Features
✅ FastAPI backend with multiple endpoints
✅ LangGraph-powered AI chatbot (GPT-4)
✅ OTP email verification system
✅ .env file support for API keys
✅ Deployable on Render

📂 Project Structure
bash
Copy
Edit
historical_ai_bot/
│── .venv/                 # Virtual environment (optional)
│── app/                   # Main application folder
│   ├── chatbot.py         # AI chatbot logic (LangGraph)
│   ├── email_otp.py       # OTP email verification
│   ├── main.py            # FastAPI app (API endpoints)
│── requirements.txt       # Dependencies
│── .env                   # Environment variables
│── README.md              # Documentation
│── run.sh                 # Bash script to start the app
│── deploy.md              # Deployment guide
🛠️ Installation Guide
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/historical_ai_bot.git
cd historical_ai_bot
2️⃣ Create & Activate Virtual Environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file and add:

ini
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
EMAIL_SENDER=your_email@example.com
EMAIL_PASSWORD=your_email_password
🚀 Running the App
Locally
bash
Copy
Edit
uvicorn app.main:app --reload
Visit http://127.0.0.1:8000/docs to test APIs.

On Render
See deploy.md for detailed deployment steps.

🖥️ API Endpoints
Endpoint	Method	Description
/chat/	POST	AI chatbot API (LangGraph + OpenAI GPT)
/send-otp/	POST	Send OTP to email
/verify-otp/	POST	Verify OTP
🛠️ Technologies Used
FastAPI – High-performance API framework
LangChain & LangGraph – AI-powered conversation logic
Pydantic – Data validation
Uvicorn – ASGI server
Email-validator – OTP email verification
💡 Contributing
Fork the repo
Create a new branch (git checkout -b feature-branch)
Commit changes (git commit -m "Added feature")
Push to GitHub (git push origin feature-branch)
Open a Pull Request
📜 License
This project is licensed under the MIT License.

📬 Contact
For issues, create a GitHub Issue or contact me via email: your-email@example.com.

🚀 Happy Coding! 😊
