import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
import re
import bcrypt 

import databases.database_user as db
import pages.app as app


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
        password = st.text_input(label="Password", type='password').encode("utf-8")
        submitted = st.form_submit_button("Login")

        if submitted:
            if (email_regexp.match(email) == None):
                st.warning("Please provide a correct email")

            else:
                user = db.retrieve_user(email)
                if (user == None or bcrypt.checkpw(password, user["password"]) == False):
                    st.warning("Email/Password is incorrect")

                else:
                    if 'user_email' not in st.session_state:
                        st.session_state["user_email"] = email
                        st.session_state["user_username"] = db.retrieve_user(email)["username"]
                    st.success("User Found")

                

if selected == "Register":

    with st.form(key="user_registration_form", clear_on_submit = True):

        email_regexp = re.compile(r"[^@]+@[^@]+\.[^@]+")

        st.title('Join our community')
        username = st.text_input(label="Username")
        name = st.text_input(label="Name")
        surname = st.text_input(label="Surname")
        email = st.text_input(label="Email")
        password = st.text_input(label="Password", type='password').encode("utf-8")
        score = 0
        account_type = 'Basic'

        submitted = st.form_submit_button("Register")

        if submitted:
            if (email_regexp.match(email) == None):
                st.warning("Please provide a correct email")

            else:
                
                hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

                new_user = {
                    "email": email,
                    "username": username,
                    "name": name,
                    "surname": surname,
                    "password": hashed_password,
                    "score": score,
                    "account_type": account_type 
                }

                db.insert_user(new_user)
                st.success("User correctly registered! Log in and enjoy!")
    