import streamlit as st
import pdfplumber
from utils import split_documents_dict, extract_query_results

st.title("Document Research & Theme Identification Chatbot!")
st.write("Upload documents and process them here.")

uploaded_files = st.file_uploader("Upload Documents", accept_multiple_files=True)

if uploaded_files:
    st.write("Files uploaded:", [file.name for file in uploaded_files])
    files_dict = {}
    if uploaded_files:
        for file in uploaded_files:
            st.subheader(f"**Contents of {file.name}:**")
            if file.type == "application/pdf":
                with pdfplumber.open(file) as pdf:
                    text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
                    files_dict[file.name] = text
            elif file.type == "text/plain":
                text = file.getvalue().decode("utf-8")
                files_dict[file.name] = text
        # st.text_area("Extracted Text:", extracted_text, height=300)

        #########################################
        print(files_dict)
        vector_storage = split_documents_dict(files_dict)
        results = extract_query_results(vector_storage, query="")
        ##########################################

        # Submit button
        if st.button("Submit"):
            # st.session_state["extracted_text"] = extracted_text  # Store text for chatbot
            st.page_link("pages/chatbot_ui.py")







