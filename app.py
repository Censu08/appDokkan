import streamlit_authenticator as stauth
import streamlit as st
from streamlit_option_menu import option_menu

import insert_card as ic
import visualize_card as vc

# -------- SETTINGS -----------
page_title = "Welcome to Card Section"
page_icon = ":flower_playing_cards:" # emoji in webfx
# -----------------------------


st.set_page_config(page_title=page_title, page_icon=page_icon)
st.title(page_title + " " + page_icon)


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
        