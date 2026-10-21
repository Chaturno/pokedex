import sqlite3

def get_connection():
    connexion = sqlite3.connect("pokemon.db")
    try:
        yield connexion
    finally:
        connexion.close()