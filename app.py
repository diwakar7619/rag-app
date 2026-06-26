import streamlit as st
import os

st.title("RAG APP")


files = os.listdir("data")

selected_file = st.selectbox("Choose a document", files)

with open("data/" + selected_file, "r") as file:
    text = file.read()

st.write(text)
