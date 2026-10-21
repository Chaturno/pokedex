import sqlite3

def import_from_api_2_db(pokemon: Pokemon):
     connection = sqlite3.connect("pokedex.db")
     cursor = connection.cursor()
     cursor.execute(
     "INSERT INTO Pokemon (number, name, name_fr, types, image_url, height, weight, evolves_from_number) VALUES (?,?,?,?,?,?,?,?)",
     pokemon.number,pokemon.name,pokemon.name_fr,pokemon.types,pokemon.image_url,pokemon.height,pokemon.weight,pokemon.evolves_from_number)
     connection.commit()
     connection.close()