import os

from deta import Deta
from dotenv import load_dotenv

load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY_CARD")

#Deta object
deta = Deta(DETA_KEY)

#Create connection
db = deta.Base("dokkan_users")

def insert_card(card: dict):
    return db.put({
        "key": card["username"],
        "name": user["name"],
        "password": user["password"]
    })

def fetch_all_cards():
    #returns a list of JSON obj
    res = db.fetch()
    return res.items

def get_card(username):
    #return only the info for that username
    return db.get(username)

def update_card(username, updates):
    #updates is a dict with all the changes
    return db.update(updates, username)

def delete_card(username):
    return db.delete(username)