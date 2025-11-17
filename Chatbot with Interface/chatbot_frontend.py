import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import time

CONFIG = {"configurable" : {"thread_id" : "1"}}

if "message_histroy" not in st.session_state:
    st.session_state['message_histroy'] = []

for message in st.session_state['message_histroy'] :
    with st.chat_message(message['role']):
        st.text(message['contant'])

user_input = st.chat_input('Type Here...')

if user_input:
    st.session_state['message_histroy'].append({'role' : 'user', 'contant' : user_input})
    
    with st.chat_message('user'):
        st.text(user_input)


    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            (time.sleep(0.02), messsage_chunk.content)[1] 
            for messsage_chunk,  metadata in chatbot.stream(
                {'message' : [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )
    st.session_state['message_histroy'].append({'role' : 'assistant', 'contant' : ai_message})