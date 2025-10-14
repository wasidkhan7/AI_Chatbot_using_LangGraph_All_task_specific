# 💬 LangGraph Chatbot — AI Assistant with Memory and Streamlit UI  
# AI_Chatbot_using_LangGraph_All_task_specific

AI Chatbot using langGraph which can give you any answer concisely with precision



A fully functional **AI Chatbot** built using **LangGraph**, **LangChain**, and **Streamlit**, integrated with **OpenAI’s GPT-4o-mini** model.  
It’s designed for real-world use — remembers past conversations, handles context dynamically, and provides precise answers to any user query.

---

## 🚀 Features  

### 🧠 Core AI Logic
- **LLM Integration:** Uses `ChatOpenAI` from `langchain_openai` with the model `gpt-4o-mini` for intelligent responses.  
- **Graph-based Flow:** Built using LangGraph’s `StateGraph`, providing modular, node-based conversational control.  
- **State Management:** Each node maintains its own state via `TypedDict` and `add_messages` reducer.  
- **Dynamic Conversation Handling:** Chat flow moves automatically between defined nodes (`START` → `chat_node` → `END`).

### 💾 Memory System
- **Checkpointer Enabled:** Uses `InMemorySaver` from `langgraph.checkpoint.memory` for storing conversation states.  
- **Thread-specific Persistence:** Every session uses a unique `thread_id`, allowing separate conversation threads.  
- **Expandable Design:** Checkpointer can easily be upgraded to a persistent memory backend (e.g., Redis, SQLite).

### 🧩 Backend (LangGraph + OpenAI)
- `langgraph_backend.py` handles:
  - Node definition (`chat_node`)
  - State management  
  - Graph compilation  
  - LLM interaction logic  
- Automatically updates conversation memory using LangGraph’s reducer mechanism (`add_messages`).

### 🖥️ Frontend (Streamlit UI)
- `streamlit_frontend.py` provides:
  - **Interactive Chat Interface** using Streamlit components (`st.chat_message`, `st.chat_input`).
  - **Session-based Memory** using `st.session_state` for conversation continuity.
  - **Clean UI Layout:** Displays both user and assistant messages distinctly.
  - **Loading Spinners:** Provides visual feedback during API responses.
  - **Thread Initialization:** Automatically creates and manages `thread_id` for each chat.

### 🔁 Conversation Flow
1. User enters a message in Streamlit UI.  
2. Message is stored and passed to LangGraph backend.  
3. Backend LLM node (`chat_node`) processes the query using GPT-4o-mini.  
4. Response is appended to the state and displayed in the chat window.  
5. Memory is updated for future turns within the same thread.  

---
<img width="1788" height="847" alt="image" src="https://github.com/user-attachments/assets/bbc0c11c-0c0f-4a61-ae40-c6562c66786a" />

<img width="1775" height="839" alt="image" src="https://github.com/user-attachments/assets/3d7fe078-f328-43c3-a7d8-44dd74a657d7" />






## ⚙️ Technical Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3.10+ |
| Framework | LangGraph + Streamlit |
| LLM | OpenAI GPT-4o-mini |
| Memory | LangGraph Checkpointer (`InMemorySaver`) |
| UI | Streamlit Components (`st.chat_message`, `st.chat_input`) |
| Environment | .env file for API key management but i hanvt pushed it here because it is secret key |

---

#### Run backend
python langgraph_backend.py

#### Run front end
streamlit run streamlit_frontend.py

MIT License © 2025 — Open for educational and non-commercial use.

🤖 Author
Wasid Khan
💼 AI | LangGraph | Streamlit | Python Developer
