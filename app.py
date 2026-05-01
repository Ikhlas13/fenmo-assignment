import streamlit as st

st.title("Fenmo Assignment App")

st.write("This is my working application")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello {name}!")
