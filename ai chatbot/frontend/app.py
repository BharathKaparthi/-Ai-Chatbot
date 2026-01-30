import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot Using LLMs")

user_input = st.text_input("Enter your message")

if st.button("Send"):
    if user_input.strip() != "":
        response = requests.post(API_URL, json={"message": user_input})
        if response.status_code == 200:
            st.success(response.json()["reply"])
        else:
            st.error("Backend error")
    else:
        st.warning("Please enter a message")
import time
import requests

API_URL = "http://127.0.0.1:8000/chat"

# Wait 2 seconds to make sure backend is ready
time.sleep(2)

response = requests.post(API_URL, json={"message": user_input})

