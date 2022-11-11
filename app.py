import streamlit_authenticator as stauth
import streamlit as st

import database as db

users = db.fetch_all_users()

usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
hashed_passwords = [user["password"] for user in users]

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "app_dokkan", "cookie_key_impossible")

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username or password is incorrect")

if authentication_status == None:
    st.warning("Please enter a valid username/password")

if authentication_status:
    st.success("Valid!")