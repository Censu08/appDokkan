import pickle
from pathlib import Path 

import streamlit_authenticator as stauth

names = ["simone"]
username = ["censu"]
password = ["123"]

hashed_password = stauth.Hasher(password).generate()

file_path = Path(__file__).parent / 'hashed_pw.pkl'

with file_path.open("wb") as file:
    pickle.dump(hashed_password, file)