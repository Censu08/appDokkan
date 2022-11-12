import streamlit as st
from streamlit_option_menu import option_menu

import database_card as db


def visualize():
    st.title("List of all cards")

    "---"

    all_cards = db.fetch_all_cards()

    for item in all_cards:
        st.header(item["name"])
        st.subheader(item["key"])
        
        col_expander = st.expander("More details")
        with col_expander:
            st.header(item["name"])
            st.markdown("Tipology: " + item["side"] + " " + item["type_card"])
            st.markdown("Rarity: " + item["rarity"] + " " + item["banner"])

        col1, col2 = st.columns((8,1))

        with col1:
            st.text("ciao")

        with col2:
            delete_button = st.button('Delete', key= item["key"] + "_key_delete")
            # TODO: fare in modo che il bottone si refreshi al click

            
        if delete_button:
                key = item["key"]
                db.delete_card(key)
                st.success('Card successfully deleted!')
                
        "---"
        
        
        