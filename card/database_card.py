import os

from deta import Deta
from dotenv import load_dotenv

load_dotenv(".env")
DETA_KEY = os.getenv("DETA_KEY_CARD")

#Deta object
deta = Deta(DETA_KEY)

#Create connection
db = deta.Base("dokkan_cards")

def insert_card(card: dict):
    return db.put({
        "key": card["title"],
        "name": card["name"],
        "side": card["side"],
        "type_card": card["type_card"],
        "banner": card["banner"],
        "rarity": card["rarity"],
        "score": card["score"],
    })

def fetch_all_cards():
    #returns a list of JSON obj
    res = db.fetch()
    return res.items

def get_card(title):
    #return only the info for that username
    return db.get(username)

def update_card(title, updates):
    #updates is a dict with all the changes
    return db.update(updates, username)

def delete_card(title):
    return db.delete(title)