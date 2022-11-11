import pickle
from pathlib import Path

import streamlit_authenticator as stauth
import streamlit as st

names = ["simone"]
username = ["censu"]


file_path = Path(__file__).parent / 'hashed_pw.pkl'
with file_path.open("rb") as file:
    hashed_password = pickle.load(file)

authenticator = stauth.Authenticate(names, username, hashed_password, "app_dokkan", "cookie_key_impossible")

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username or password is incorrect")

if authentication_status == None:
    st.warning("Please enter a valid username/password")

if authentication_status:
    st.success("Valid!")