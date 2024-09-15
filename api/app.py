from fastapi import FastAPI
from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Langchain Demo with LLama3 API",
    description="A simple FastAPI server for interacting with Langchain's LLM",
    version="1.0"
)


llm = Ollama(model="llama3.1")

prompt1 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 200 words")

add_routes(
    app,
    prompt1|llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost.", port=os.getenv("PORT", 8000))