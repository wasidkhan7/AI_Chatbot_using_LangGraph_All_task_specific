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

        
    