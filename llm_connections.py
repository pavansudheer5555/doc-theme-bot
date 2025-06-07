groq_api_key = "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"

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    groq_api_key = groq_api_key
    # other params...
)