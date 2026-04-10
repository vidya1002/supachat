# 🚀 SupaChat

SupaChat is a conversational analytics app where users can query data using natural language.

Example queries:

* "Top trending topics"
* "Compare engagement by topic"

---

## 🧠 How It Works

User → Frontend → Backend → SQL → Response → UI

---

## 🛠️ Tech Stack

* Frontend: Next.js
* Backend: FastAPI
* API Calls: Axios

---

## ⚙️ Features

* Chat-based interface
* Natural language to SQL (basic mapping)
* API integration
* JSON response display

---

## ▶️ Run Locally

### Backend

cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn
uvicorn main:app --reload

Runs at: http://127.0.0.1:8000

---

### Frontend

cd frontend
npm install
npm run dev

Runs at: http://localhost:3000

---

## 🔌 API

POST /query

Example:
{
"user_query": "top trending topics"
}

---

## 🚧 Future Improvements

* AI-based query generation
* Supabase integration
* Charts & analytics
* Docker & deployment
* CI/CD pipeline

---

## 🎥 Demo

(Add your video link here)

---

## 👤 Author

Vidya Shree
https://github.com/vidya1002

---
