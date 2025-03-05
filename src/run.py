import streamlit as st


st.title("Pytopia Dashboard")

with st.sidebar:
    login_status = st.radio(options=["Login", "Sign Up"], label="Login/Signup")
    if login_status == "Login":
        st.text_input(label="Username", placeholder='Enter your username')
        st.text_input(label="Password", placeholder='Enter your password')
    else:
        st.text_input(label="Choose a username", placeholder="Username")
        st.text_input(label="Choose a email", placeholder="Email")
        st.text_input(label="Write a password", placeholder="Password")


with st.expander(label="Doc"):
    st.file_uploader(label="Choose a file")
