import nbimporter
import streamlit as st
from Query_handling import query


def run_rag_interface():
    st.title("Local RAG Chatbot")
    st.write("Please Enter your query below and get responses from the local embeddings.")

    user_query = st.text_input("Your Query:", placeholder="Pleae provide your query here.")

    if st.button("Submit"):
        if user_query.strip():
            with st.spinner("Retrieving your Answer"):
                try:
                    response = query(user_query)
                    st.success("Response received!")
                    st.write(f"**Answer:** {response}")
                except Exception as e:
                    st.error("An error occurred.")
                    st.write(f"**Error Details:** {e}")
        else:
            st.warning("Please enter a valid query.")

if __name__ == "__main__":
    run_rag_interface()
