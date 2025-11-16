from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage
import os

llm = ChatOpenAI(api_key=os.getenv('API_KEY'), base_url='https://lightning.ai/api/v1/')

class ChatState(TypedDict):
    message : Annotated[list[BaseMessage], add_messages]

def chat_node(state : ChatState):
    message = state['message']
    response = llm.invoke(message)
    return {"message" : [response]}


graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

checkpointer = InMemorySaver()
chatbot = graph.compile(checkpointer=checkpointer)