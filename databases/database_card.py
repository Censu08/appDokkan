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
card_collection = mongo_db["dokkan_cards"]


def insert_card(card: dict):
    return card_collection.insert_one(card)

def retrieve_all_cards():
    
    cards_list = card_collection.find()

    return list(cards_list)

def delete_card(title: str):
    return card_collection.delete_one({ "title": title })