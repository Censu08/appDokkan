import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

import databases.database_card as db_c
import databases.database_card_user as db_c_u

if "button_clicked_choose" not in st.session_state:
    st.session_state.button_clicked_choose = False

def callback_choose_open():
    st.session_state.button_clicked_choose = True

def callback_choose_close():
    st.session_state.button_clicked_choose = False

if "button_clicked_upgrade" not in st.session_state:
    st.session_state.button_clicked_upgrade = False

def callback_upgrade_open():
    st.session_state.button_clicked_upgrade = True

def callback_upgrade_close():
    st.session_state.button_clicked_upgrade = False

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
            add_button = st.button('Choose card', key= item["title"] + "_key_add",  on_click=callback_choose_open)

        with col2:
            delete_button = st.button('Delete', key= item["title"] + "_key_delete")
            # TODO: fare in modo che il bottone si refreshi al click

            
        if delete_button:
                title_card = item["title"]
                db_c.delete_card(title_card)
                st.success('Card successfully deleted!')

        if st.session_state.button_clicked_choose:
                if len(db_c_u.retrieve_one_card(st.session_state["user_email"], item["title"])) == 0:
                    
                    ability = st.number_input('Insert the ability', key= item["title"] + "key_input_ability", min_value=0, max_value=4)
                    ability_button = st.button('Add to collection', key= item["title"] + "key_add_ability")
                    if ability_button:
                        final_score = (ability * 0.5 + 1) * item["score"]
                        if ability == 4:
                            final_score = final_score + 0.5 * item["score"]
                        user_card = {
                            "utente": st.session_state["user_email"],
                            "title": item["title"],
                            "name": item["name"],
                            "score": item["score"],
                            "final_score": final_score,
                            "rarity": item["rarity"],
                            "banner": item["banner"]
                        }
                        db_c_u.insert_card_user(user_card)
                        callback_choose_close()
                        st.success("Card successfully inserted! Check -My Cards- section")
                else:
                    st.warning("Card aready inserted!")
        "---"
        
        
def visualize_user_card(user_email: str):

    all_cards = db_c_u.retrieve_all_cards(user_email)
    all_cards_df = pd.DataFrame(all_cards)

    score = "0"

    if len(all_cards_df) > 0:
        all_cards_df.drop(['_id', 'utente'], axis=1, inplace=True)
        final_score = str(all_cards_df["final_score"].sum())

    container_1 = st.container()
    with container_1:
        container_1.title("You total points are: " + final_score)

        container_col_expander = st.expander("See summary table")
        with container_col_expander:
            st.dataframe(all_cards_df)
    
    container_2 = st.container()
    with container_2:
        container_2.title("List of cards")

        item_col_expander = st.expander("See list of cards")
        with item_col_expander:
        
            for item in all_cards:
                st.header(item["name"])
                st.subheader(item["title"])
                st.subheader(item["rarity"])
                st.subheader(item["banner"])
                score = item["score"] 
                st.markdown(f"Score of the card: {score}")

                col1, col2 = st.columns((7.5,1))

                with col1:
                    upgrade_button = st.button('Upgrade', key= item["title"] + "_key_upgrade", on_click=callback_upgrade_open)

                with col2:
                    delete_button = st.button('Delete', key= item["title"] + "_key_delete")
                    # TODO: fare in modo che il bottone si refreshi al click

                    
                if delete_button:
                    db_c_u.delete_card(st.session_state["user_email"], item["title"])
                    st.success("Card Deleted")

                if st.session_state.button_clicked_upgrade:
                    st.write("Upgrade Card")

                    ability = st.number_input('Insert the ability', key= item["title"] + "key_input_ability", min_value=0, max_value=4)
                    ability_button = st.button('Upgrade card', key= item["title"] + "key_add_ability")
                    if ability_button:
                        final_score = (ability * 0.5 + 1) * item["score"]
                        if ability == 4:
                            final_score = final_score + 0.5 * item["score"]
                        user_card = {
                            "utente": st.session_state["user_email"],
                            "title": item["title"],
                            "name": item["name"],
                            "score": final_score,
                            "rarity": item["rarity"],
                            "banner": item["banner"]
                        }
                        db_c_u.update_card_user(item["title"], final_score)
                        callback_upgrade_close()

                        st.success("Card successfully upgraded")
                "---"