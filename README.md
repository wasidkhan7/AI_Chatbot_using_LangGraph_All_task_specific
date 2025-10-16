# 💬 LangGraph Chatbot — AI Assistant with Memory and Streamlit UI  
# 💬 AI Chatbot using LangGraph + Streamlit + OpenAI + SQLite

### 🧠 A full-stack conversational chatbot project built 

---

## 📑 Project Overview
This project is an intelligent chatbot built using **LangGraph**, **LangChain**, **OpenAI API**, and **Streamlit** as frontend.  
The chatbot can:
- Remember previous conversations using **SQLite memory (checkpoints)**
- Allow users to **start, resume, or delete** conversation threads
- Auto-generate **titles for each chat**
- Handle **streaming chat responses**
- Store all messages persistently in the **database**
- Support **document upload and voice transcription (optional features)**

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|----------------|
| **Frontend** | Streamlit |
| **Backend** | LangGraph + LangChain + OpenAI |
| **Database** | SQLite |
| **LLM Model** | GPT-4o-mini (via OpenAI API) |
| **Memory** | SqliteSaver (persistent checkpointing) |

---

## 🚀 Features

✅ **Persistent Conversations:**  
All chat sessions are automatically saved in SQLite database.

✅ **Sidebar with Threads:**  
View all previous chats, resume them, or delete specific ones.

✅ **Auto Chat Titles:**  
Each conversation is automatically named based on your first message.

✅ **Streaming Responses:**  
LLM responses appear in real-time, providing a smooth user experience.

---
## 🧱 System Architecture

Frontend (Streamlit)
↓
Backend (LangGraph + LangChain)
↓
OpenAI GPT-4o-mini API
↓
SQLite Database (Persistent Memory + Topics)


## 📂 Project Structure
📦 Chatbot_FYP
├── langgraph_backend.py # Backend logic (LangGraph, SQLite, Checkpointing)
├── Front_app.py # Streamlit Frontend
├── chatbot_Database.db # SQLite Database
├── requirements.txt
├── README.md
└── .env # Contains OPENAI_API_KEY which is seccret key

## ⚙️ Installation and Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/LangGraph-Chatbot-FYP.git
   cd LangGraph-Chatbot-FYP

   pip install -r requirements.txt

🧠 Use Cases

Interactive AI-based personal assistant

Educational chatbot for Q&A

Internal team assistant for documents

Customer support prototype


#### Run backend
python langgraph_backend.py

#### Run front end
streamlit run streamlit_frontend.py

MIT License © 2025 — Open for educational and non-commercial use.


🧑‍💻 Author
Wasid Khan
📍 BS Computer Science | University of Peshawar
🔗 LinkedIn Profile

🌐 GitHub: github.com/wasidkhan7
💼 AI | LangGraph | Streamlit | Python Developer
