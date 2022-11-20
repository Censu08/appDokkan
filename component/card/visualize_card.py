import streamlit as st
from streamlit_option_menu import option_menu

import databases.database_card as db_c
import databases.database_card_user as db_c_u


def visualize():
    st.title("List of all cards")

    "---"

    all_cards = db_c.retrieve_all_cards()

    for item in all_cards:
        st.header(item["name"])
        st.subheader(item["title"])
        
        col_expander = st.expander("More details")
        with col_expander:
            st.header(item["name"])
            st.markdown("Tipology: " + item["side"] + " " + item["type_card"])
            st.markdown("Rarity: " + item["rarity"] + " " + item["banner"])
            score = item["score"] 
            st.markdown(f"Score of the card: {score}")

        col1, col2 = st.columns((8,1))

        with col1:
            add_button = st.button('Add to collection', key= item["title"] + "_key_add")

        with col2:
            delete_button = st.button('Delete', key= item["title"] + "_key_delete")
            # TODO: fare in modo che il bottone si refreshi al click

            
        if delete_button:
                title_card = item["title"]
                db_c.delete_card(title_card)
                st.success('Card successfully deleted!')

        if add_button:

                if len(db_c_u.retrieve_one_card(item["title"])) == 0:
                    user_card = {
                        "utente": st.session_state["email"],
                        "title": item["title"],
                        "name": item["name"],
                        "score": item["score"],
                        "rarity": item["rarity"],
                        "banner": item["banner"]
                    }
                    db_c_u.insert_card_user(user_card)
                    st.write(user_card)

                else:
                    st.warning("Card aready inserted!")
        "---"
        
        
def visualize_user_card():

    all_cards = db_c_u.retrieve_all_cards()

    for item in all_cards:
        st.header(item["name"])
        st.subheader(item["title"])
        
        col_expander = st.expander("More details")
        with col_expander:
            st.subheader(item["rarity"])
            st.subheader(item["banner"])
            score = item["score"] 
            st.markdown(f"Score of the card: {score}")

        col1, col2 = st.columns((8,1))

        with col1:
            upgrade_button = st.button('Upgrade', key= item["title"] + "_key_upgrade")

        with col2:
            delete_button = st.button('Delete', key= item["title"] + "_key_delete")
            # TODO: fare in modo che il bottone si refreshi al click

            
        if delete_button:
                st.write("Delete Card")

        if upgrade_button:
                st.write("Upgrade Card")
        "---"