import requests
import streamlit as st

def get_ollama_response(input_text):
    response = requests.post(
        'http://localhost:8000/poem/invoke',
        json={"input": {"topic": input_text}}
    )
    return response.json()['output']

st.title('Langchain Demo with LLama3 API')
input_text = st.text_input("Write an poem on")

if input_text:
    st.write(get_ollama_response(input_text))

