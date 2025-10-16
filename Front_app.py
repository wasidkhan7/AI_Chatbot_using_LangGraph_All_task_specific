import streamlit as st 
from langchain_core.messages import BaseMessage , HumanMessage , AIMessage
from langgraph_backend import chatbot, retrieve_all_threads ,save_chat_topic, get_all_chat_topics, delete_chat_thread
import uuid  # used to create threads id randomly

st.title("💬 Lets Chat With My Chatbot")
st.caption("Chatbot using LangGraph + Streamlit + OpenAI")

#                          ****** utility functions ****

# generating random thread_id using uuid
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

# function to start new conversation
def reset_chat():
    thread_id = generate_thread_id()
    st.session_state.thread_id = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state.message_history = []

# making thread_ids for all chats
def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state.chat_threads.append(thread_id)

# making a function which gives the chat history on the basis of thread_id when click on that thread_id
def load_conversation(thread_id):
    try:
        state_data = chatbot.get_state(config={"configurable": {"thread_id": thread_id}})
        # Safely handle case where 'messages' key is missing
        if "messages" in state_data.values:
            return state_data.values["messages"]
        else:
            return []  # Return empty list if no messages yet
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error loading conversation for thread {thread_id}: {e}")
        return []


#               ******************* session setup  *******************

# Initialize chat history
if "message_history" not in st.session_state:
    st.session_state.message_history = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]

# adding threadid to session    
if "thread_id" not in st.session_state:
    st.session_state.thread_id = generate_thread_id()

# thread_ids for all chats into a list
if "chat_threads" not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_threads()  # just this line got updated for Sqlite databse in frontend

# store topics (titles) for each thread
if "chat_topics" not in st.session_state:
    st.session_state["chat_topics"] = get_all_chat_topics()    # stores the title for each chat

# adding thread_id to the session
add_thread(st.session_state['thread_id'])


#             ********************* sidebar UI *************************    

st.sidebar.title("MyChatbot")

if st.sidebar.button("Start New Chat"):
    reset_chat()  # calling start conversation function

st.sidebar.header("My Conversations")

# it shows all the running threads in sidebar + each chat row with delete button 
# ✅ UPDATED — each chat row with delete button
for thread_id in st.session_state['chat_threads'][::-1]:
    topic_label = st.session_state["chat_topics"].get(thread_id, str(thread_id))

    cols = st.sidebar.columns([0.8, 0.2])  # title | delete button side by side
    with cols[0]:
        if st.button(topic_label, key=f"open_{thread_id}"):
            st.session_state.thread_id = thread_id
            chat_messages = load_conversation(thread_id)

            temp_messages = []
            for msg in chat_messages:
                if isinstance(msg, HumanMessage):
                    role = "user"
                else:
                    role = "assistant"
                temp_messages.append({"role": role, "content": msg.content})
            st.session_state['message_history'] = temp_messages

    with cols[1]:
        if st.button("🗑️", key=f"delete_{thread_id}"):
            delete_chat_thread(thread_id)  #  remove from DB
            if thread_id in st.session_state['chat_threads']:
                st.session_state['chat_threads'].remove(thread_id)
            if thread_id in st.session_state['chat_topics']:
                del st.session_state['chat_topics'][thread_id]
            if st.session_state.thread_id == thread_id:
                reset_chat()  #  start fresh if deleted current chat
            st.rerun()  #  refresh UI instantly


#             ****************** UI FOR Chatbot **********************
# Display chat history
for msgs in st.session_state.message_history:
    with st.chat_message(msgs["role"]):
        st.markdown(msgs["content"])

# Chat input
if user_input := st.chat_input("Type your message..."):
    # Add user message
    st.session_state.message_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # create a topic from the first user message in this thread
    if st.session_state.thread_id not in st.session_state["chat_topics"]:
        topic_name = " ".join(user_input.strip().split(" ")[:4]).capitalize() + "..."
        st.session_state["chat_topics"][st.session_state.thread_id] = topic_name
        save_chat_topic(st.session_state.thread_id, topic_name)  # persist in databas

    # Prepare state
    state = {"messages": [HumanMessage(content=user_input)]}

    # making chatbot streamable, we used .stream instead of invoke 
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                state,
                config={"configurable": {"thread_id": st.session_state.thread_id}},
                stream_mode="messages"
            )
        )

    st.session_state.message_history.append({"role": "assistant", "content": ai_message})
