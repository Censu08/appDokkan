import streamlit_authenticator as stauth
import streamlit as st
from streamlit_option_menu import option_menu

import database_user as db


# ---------- NAVIGATION MENU -----------------
selected = option_menu(
        menu_title = None, 
        options = ["Login", "Register"],
        icons = ["door-open", "book"], #icons.getbootstrap.com
        orientation = "horizontal")




if selected == "Login":

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
        st.write("Valid!")



if selected == "Register":

    with st.form(key="registration_form"):
        st.title('Register')
        username = st.text_input(label="Enter Username")
        name = st.text_input(label="Enter Name")
        password = st.text_input(label="Enter Password", type="password")

        new_user = {
            "username": username,
            "name": name,
            "password": password
        }

        submitted = st.form_submit_button("Register")

        if submitted:
            users = db.fetch_all_users()

            if username not in [user["key"] for user in users]:
                db.insert_user(new_user)
                st.success('Welcome!')

            else:
                st.warning('Already existing user! Try to log in')