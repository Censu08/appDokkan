from pymongo import MongoClient
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()
CLIENT = os.getenv('CLIENT_MONGO')

@st.experimental_singleton(suppress_st_warning=True)
def init_connection():
    return MongoClient(CLIENT)

mongo_client = init_connection()
mongo_db = mongo_client["dokkan_application"]
user_card_collection = mongo_db["dokkan_user_cards"]


def insert_card_user(user_card: dict):
    return user_card_collection.insert_one(user_card)

def retrieve_all_cards(email: str()):
    cards_list = user_card_collection.find({"utente": email})

    return list(cards_list)

def retrieve_one_card(email: str, title: str):
    return list(user_card_collection.find({"utente": email, "title": title}))

def delete_card(email: str, title: str):
    return user_card_collection.delete_one({"utente": email, "title": title})