import streamlit as st

st.title("🤖 Chatbot UI")

if "extracted_text" in st.session_state:
    st.write("Document content loaded for chat!")

user_input = st.text_input("Ask a question about the document:")

if user_input:
    st.write("🚀 You asked:", user_input)
    # Here, you can integrate NLP or LLM for responses