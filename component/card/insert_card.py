import streamlit as st
from streamlit_option_menu import option_menu

import databases.database_card as db

def insert():
    with st.form(key="card_insert_form", clear_on_submit = True):
        st.title('Insert a card')
        name = st.text_input(label="Enter card name")
        title = st.text_input(label="Enter card title")

        possible_sides= ('Super', 'Extreme')
        possible_types= ('PHY', 'STR', 'INT', 'TEQ', 'AGL')
        possible_banners= ('DokkanFest', 'Legendary', 'Carnival')
        possible_rarity= ('tUr' , 'Rare', 'LR')

        side = st.selectbox('Choose the side picked by the character', possible_sides)
        type_card = st.selectbox('Choose the type of the character', possible_types)
        banner = st.selectbox('Choose the banner type of the card', possible_banners)
        rarity = st.selectbox('Choose the rarity of the card', possible_rarity)
        
        submitted = st.form_submit_button("Insert")

        if rarity == 'LR':
            
            if banner == 'DokkanFest':
                score = 2

            elif banner == 'Carnival':
                score = 2
            
            else:
                score = 1.5

        elif rarity == 'tUr':
            if banner == 'DokkanFest':
                score = 1
            
            else:
                st.warning('Banner and rarity combiantion not allowed, stupido mahallah')

        else:
            score = 0.75

        if submitted:
            try: 
                new_card = {
                    "title": title,
                    "name": name,
                    "super_attack": super_attack,
                    "side": side,
                    "type_card": type_card,
                    "banner": banner,
                    "rarity": rarity,
                    "score": score
                }

                db.insert_card(new_card)
                st.success('Card succesfully inserted')

            except:
                pass