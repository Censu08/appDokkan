from pymongo import MongoClient
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()
CLIENT = os.getenv('CLIENT_MONGO')

@st.experimental_singleton(suppress_st_warning=True)
def init_connection():
    st.header(CLIENT)
    return MongoClient(CLIENT)

mongo_client = init_connection()
mongo_db = mongo_client["dokkan_application"]
user_collection = mongo_db["dokkan_users"]


def insert_user(user: dict):
    return user_collection.insert_one(user)

def retrieve_user(email: str):
    
    user_to_find = {
        "email": email
    }

    user = user_collection.find_one(user_to_find)
    return user