<<<<<<< HEAD
from langgraph.graph import StateGraph, START,  END
from langchain_openai import  ChatOpenAI 
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage , HumanMessage
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver #saves conv in memory(RAM)
from langgraph.graph.message import add_messages # use to add all messages
import os


load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))


# define  a state 
class ChatState(TypedDict): 
    messages : Annotated[list[BaseMessage], add_messages ] # all messages will be added(work aS reducer)
    
# making node function for chat
def chat_node(state: ChatState): 
    # user query
    messages= state['messages']
    # send to llm
    response = llm.invoke(messages)
    #response resturn state
    return {"messages": [response]} 
   # puuting respoonse in list because we are appending messages in in list in  a STATE
   
    
# persistence memory 
checkpointer = InMemorySaver()


# DEFINE A graph
graph= StateGraph(ChatState)

# add nodes
graph.add_node( "chat_node", chat_node)


#add edges
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

# compile the graph
chatbot= graph.compile(checkpointer=checkpointer)

        
=======
from langgraph.graph import StateGraph, START,  END
from langchain_openai import  ChatOpenAI 
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage , HumanMessage
from dotenv import load_dotenv
from langgraph.checkpoint.sqlite import SqliteSaver #saves conversatoion  in database instead of  memory(RAM)
from langgraph.graph.message import add_messages # use to add all messages
import os
import sqlite3

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))


# define  a state 
class ChatState(TypedDict): 
    messages : Annotated[list[BaseMessage], add_messages ] # all messages will be added(work aS reducer)
    
# making node function for chat
def chat_node(state: ChatState): 
    # user query
    messages= state['messages']
    # send to llm
    response = llm.invoke(messages)
    #response resturn state
    return {"messages": [response]} 
   # puuting respoonse in list because we are appending messages in in list in  a STATE
   
        
    
# database
conn=sqlite3.connect(database="chatbot_Database.db", check_same_thread=False )
checkpointer = SqliteSaver(conn=conn)


# DEFINE A graph
graph= StateGraph(ChatState)

# add nodes
graph.add_node( "chat_node", chat_node)


#add edges
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

# compile the graph
chatbot= graph.compile(checkpointer=checkpointer)

# this shows you how many checkpoints are  stored in your threads / database
def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None): # bt setting none means i want all the checkpoints that are store in DB to be shown 
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    
    return list(all_threads)    



# these functions store the titles of each chat in DB

def save_chat_topic(thread_id: str, topic: str):
    """Store or update chat topic/title in a separate table."""
    conn.execute(
        "CREATE TABLE IF NOT EXISTS chat_topics (thread_id TEXT PRIMARY KEY, topic TEXT)"
    )
    conn.execute(
        "INSERT OR REPLACE INTO chat_topics (thread_id, topic) VALUES (?, ?)",
        (str(thread_id), topic),
    )
    conn.commit()


def get_all_chat_topics():
    """Retrieve all saved chat topics from the database."""
    conn.execute(
        "CREATE TABLE IF NOT EXISTS chat_topics (thread_id TEXT PRIMARY KEY, topic TEXT)"
    )
    cursor = conn.execute("SELECT thread_id, topic FROM chat_topics")
    return dict(cursor.fetchall())



# function to delete a chat thread and its topic

def delete_chat_thread(thread_id: str):
    """Delete a chat thread (checkpoints + topic) from database."""
    try:
        # Delete from LangGraph's checkpoint tables (these are the actual names used)
        conn.execute("DELETE FROM checkpoints WHERE thread_id = ?", (str(thread_id),))
        conn.execute("DELETE FROM checkpoint_blobs WHERE thread_id = ?", (str(thread_id),))

        # Delete topic from topic table if exists
        conn.execute("CREATE TABLE IF NOT EXISTS chat_topics (thread_id TEXT PRIMARY KEY, topic TEXT)")
        conn.execute("DELETE FROM chat_topics WHERE thread_id = ?", (str(thread_id),))

        conn.commit()
    except Exception as e:
        print(f"Error deleting chat thread {thread_id}: {e}")

        
>>>>>>> 0814a4c (Initial commit - Added main chatbot backend and frontend files)
    