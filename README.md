# MeetMate 🎓  
AI-Powered Meeting Transcription & Summarization Tool

MeetMate is a Python-based AI meeting assistant designed to help users
transcribe meeting audio, generate concise summaries, and share those
summaries via email.

The project focuses on helping students and professionals reduce
manual note-taking during meetings.

---

## 🚀 Features
- 🎙️ Audio transcription using Google Cloud Speech-to-Text
- ✂️ Automatic meeting summarization
- 📧 Email delivery of meeting summaries
- 🧩 Modular and clean Python architecture
- 🔐 Secure handling of environment variables and credentials

---

## 🛠️ Tech Stack
- Python 3.8+
- Google Cloud Speech-to-Text
- Pydub (audio processing)
- python-dotenv
- SMTP (email service)

---

## 📂 Project Structure
MeetMate/
├── app.py                  # Main entry point
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
├── src/
│   ├── bot.py              # Workflow controller
│   ├── transcribe.py       # Audio → Text (Google Speech-to-Text)
│   ├── summarize.py        # Text → Summary
│   ├── send_email.py       # Email sender
│   ├── .env.example        # Example environment variables
│   └── credentials.example.json  # Example Google credentials file
│
├── audio/                  # User-provided meeting audio (not uploaded)
│   └── .gitkeep
│
└── outputs/                # Generated summaries (ignored in GitHub)


---

## ⚙️ Setup Instructions

### 1️⃣ Clone or Download the Repository
git clone https://github.com/TahaShaikh018/MeetMate.git
cd MeetMate

OR download the repository as a ZIP file and extract it.

---

### 2️⃣ (Optional) Create a Virtual Environment
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux

---

### 3️⃣ Install Dependencies
pip install -r requirements.txt

---

### 4️⃣ Configure Environment Variables
Create a `.env` file using the provided `.env.example`:

GOOGLE_APPLICATION_CREDENTIALS=credentials.json
GMAIL_APP_PASSWORD=your_app_password_here

Important:
Do NOT upload `.env` or `credentials.json` to GitHub.

---

### 5️⃣ Setup Google Cloud Credentials
1. Create a Google Cloud project
2. Enable Speech-to-Text API
3. Create a service account
4. Download the service account key as `credentials.json`
5. Place it in the project root directory

---

### 6️⃣ Audio Input
Provide your own meeting audio file (e.g., `.wav` or `.mp3`) and place it
inside an `audio/` folder before running the application.

Audio files are intentionally not included in this repository.

---

### 7️⃣ Run the Application
python app.py

---

## 📌 Notes
- Audio files, credentials, and environment files are excluded for security
- Users must supply their own meeting audio
- This project is intended for educational and learning purposes

---

## 🔮 Future Enhancements
- Web-based user interface
- Real-time meeting transcription
- Multi-language support
- Calendar and meeting integrations
- Cloud deployment

---

## 👨‍💻 Author
Taha Shaikh  
B.Tech – Artificial Intelligence & Data Science  
Student Project – MeetMate
