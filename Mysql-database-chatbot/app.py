import streamlit as st 
from src.utils import MYSQLChain

st.set_page_config(page_title="Chat with Database", page_icon=":robot_face:")
st.title("MYSQL Chatbot")

# Initialize the MYSQLChain only once
if "mysql_chain" not in st.session_state:
    st.session_state.mysql_chain = MYSQLChain()
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

mode = st.radio("Choose interaction mode:", ["Agent", "Few-Shot QA"], horizontal=True)

if prompt := st.chat_input("Ask a question about the database"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        if mode == "Agent":
            response = st.session_state.mysql_chain.run_agent(prompt)
        else:
            response = st.session_state.mysql_chain.run_qa_chain(prompt)
    except Exception as e:
        response = f"Error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
