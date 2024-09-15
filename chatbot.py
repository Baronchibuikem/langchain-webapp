from langchain_community.llms import Ollama
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')


# Define the chat prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, Please respond to users query."),
        ("user", "Question:{question}"),
    ]
)

st.title('Langchain Demo With LLama3 API')
input_text = st.text_input("Search the topic you want")

# Initialize the Ollama LLM with model "llama3.1"
llm = Ollama(model="llama3.1")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))