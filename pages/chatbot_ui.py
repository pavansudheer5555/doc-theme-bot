import streamlit as st
# from utils import extract_query_results
from utils import extract_query_results

st.title("🤖 Chatbot UI")

if "extracted_text" in st.session_state:
    st.write("Document content loaded for chat!")

user_input = st.text_input("Ask a question about the document:")

if user_input:
    st.write("🚀 You asked:", user_input)
    # Here, you can integrate NLP or LLM for response
    vector_storage = st.session_state.get("vector_storage", None)
    out_res = extract_query_results(vectorstore=vector_storage, query=user_input)
    print(out_res)
    st.write(out_res)