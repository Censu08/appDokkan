import streamlit_authenticator as stauth
import streamlit as st
from streamlit_option_menu import option_menu

import insert_card 

# -------- SETTINGS -----------
page_title = "Welcome to Card Section"
page_icon = ":video_game:" # emoji in webfx
# -----------------------------


st.set_page_config(page_title=page_title, page_icon=page_icon)
st.title(page_title + " " + page_icon)


# ---------- NAVIGATION MENU -----------------
selected = option_menu(
        menu_title = None, 
        options = ["Add Card", "All Cards", "My Cards"],
        icons = ["door-open", "book"], #icons.getbootstrap.com
        orientation = "horizontal")

if selected == "Add Card":
    insert_card.insert()

            