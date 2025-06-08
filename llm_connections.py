import os
from dotenv import load_dotenv

load_dotenv()
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    groq_api_key  = os.getenv("GROQ_API_KEY")
    # other params...
)