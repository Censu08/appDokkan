import streamlit_authenticator as stauth
import streamlit as st
from streamlit_option_menu import option_menu

import component.card.insert_card as ic
import component.card.visualize_card as vc

# -------- SETTINGS -----------
page_title = "Welcome to Card Section " + st.session_state["user_username"]
page_icon = ":flower_playing_cards:" # emoji in webfx
# -----------------------------

st.title(page_icon + " " + page_title) 

def app_main():

    # ---------- NAVIGATION MENU -----------------
    selected = option_menu(
            menu_title = None, 
            options = ["Add Card", "All Cards", "My Section"],
            icons = ["plus-circle-fill", "view-list", "card-heading"], #icons.getbootstrap.com
            orientation = "horizontal")

    if selected == "Add Card":
        ic.insert()

    if selected == "All Cards":
        vc.visualize()

    if selected == "My Section":
        vc.visualize_user_card(st.session_state["user_email"])


app_main()
