import streamlit as st
from main import get_few_shot_db_chain

st.title("T Shirt Store: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)