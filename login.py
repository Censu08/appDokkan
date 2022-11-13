import streamlit_authenticator as stauth
import streamlit as st
from streamlit_option_menu import option_menu
import re

import databases.database_user as db


# ---------- NAVIGATION MENU -----------------
selected = option_menu(
        menu_title = None, 
        options = ["Login", "Register"],
        icons = ["door-open", "book"], #icons.getbootstrap.com
        orientation = "horizontal")


if selected == "Login":
    with st.form(key="user_login_form"):

        email_regexp = re.compile(r"[^@]+@[^@]+\.[^@]+")

        st.title('Enter the community')
        email = st.text_input(label="Email")
        password = st.text_input(label="Password", type='password')

        submitted = st.form_submit_button("Login")

        if submitted:
            if (email_regexp.match(email) == None):
                st.warning("Please provide a correct email")

            else:
                user = db.retrieve_user(email, password)

                if user == None:
                    st.warning("Emai/Password incorrect")

                else:
                    st.success("Found")

                

if selected == "Register":

    with st.form(key="user_registration_form"):

        email_regexp = re.compile(r"[^@]+@[^@]+\.[^@]+")

        st.title('Join our community')
        username = st.text_input(label="Username")
        name = st.text_input(label="Name")
        surname = st.text_input(label="Surname")
        email = st.text_input(label="Email")
        password = st.text_input(label="Password", type='password')
        score = 0
        account_type = 'Basic'

        submitted = st.form_submit_button("Register")

        if submitted:
            if (email_regexp.match(email) == None):
                st.warning("Please provide a correct email")

            else:
                new_user = {
                    "email": email,
                    "username": username,
                    "name": name,
                    "surname": surname,
                    "password": password,
                    "score": score,
                    "account_type": account_type 
                }

                db.insert_user(new_user)
    #new_user = {
    #    "username": "ciao",
    #    "name": "come",
    #    "password": "va"
    #}
    #db.insert_user(new_user)
    