import streamlit_authenticator as stauth
import streamlit as st
from streamlit_option_menu import option_menu

import component.card.insert_card as ic
import component.card.visualize_card as vc



# -------- SETTINGS -----------
page_title = "Welcome to Card Section " + st.session_state["username"]
page_icon = ":flower_playing_cards:" # emoji in webfx
# -----------------------------

st.title(page_icon + " " + page_title) 

def app_main():

    # ---------- NAVIGATION MENU -----------------
    selected = option_menu(
            menu_title = None, 
            options = ["Add Card", "All Cards", "My Cards"],
            icons = ["plus-circle-fill", "view-list", "card-heading"], #icons.getbootstrap.com
            orientation = "horizontal")

    if selected == "Add Card":
        ic.insert()

    if selected == "All Cards":
        vc.visualize()

    if selected == "My Cards":
        vc.visualize_user_card()

if st.session_state["logged_in"] == True:
    app_main()

else:
    st.write("Log in to enjoy the experience")