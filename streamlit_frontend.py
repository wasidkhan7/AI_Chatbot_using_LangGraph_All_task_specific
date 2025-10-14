import streamlit as st 
from langchain_core.messages import BaseMessage , HumanMessage , AIMessage
from langgraph_backend import chatbot

    
    
st.title("💬 LangGraph Chatbot")
st.caption("Chatbot using LangGraph + Streamlit + OpenAI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I assist you today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if user_input := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare state
    state = {"messages": [HumanMessage(content=user_input)]}

    # Invoke LangGraph chatbot
    result = chatbot.invoke(state, config={"configurable": {"thread_id": "chat1"}})

    # Get assistant reply
    assistant_msg = result["messages"][-1].content
    st.session_state.messages.append({"role": "assistant", "content": assistant_msg})

    with st.chat_message("assistant"):
        st.markdown(assistant_msg)