from fastapi import FastAPI
import requests
from schemas.pokemon import Pokemon
from db.database_connexion import get_connection
#from repositories.pokemon_repository import get_pokemon_by_number
from clients.pokeapi import get_pokemon_from_api, get_species_from_api, get_types_from_api
# L'import fonctionne car nous faisons appel au fichier schemas/pokemon.py puis nous récupérons la classe Pokémon

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
app = FastAPI()

@app.get("/pokemon/{number}/")
def pokemon(number: int):
    return get_pokemon_from_api(number)

@app.get("/pokemon/{number}/scan")
def pokemon(number: int):
    pokemon_data = get_pokemon_from_api(number)
    species_data = get_species_from_api(pokemon_data["species"]["url"])
    types_fr=[]
        
    for element in pokemon_data["types"]:
        types_data = get_types_from_api(element["type"]["url"])
        types_fr.append(
            next(nom["name"] for nom in types_data["names"] if nom["language"]["name"] == "fr")
        )

    pokemon = Pokemon(
        number=pokemon_data["id"],
        name=pokemon_data["name"],
        name_fr=next(nom["name"] for nom in species_data["names"] if nom["language"]["name"] == "fr"),
        types = types_fr,
        image_url=pokemon_data["sprites"]["front_default"] or "",
        height=pokemon_data["height"],
        weight=pokemon_data["weight"],
)
    return pokemon

      ##  types=[t["type"]["name"] for t in pokemon_data["types"]],

'''name_fr = pokemon_data.get(""),
        types = pokemon_data.get(""),
        image_url = pokemon_data.get(""),
        height = pokemon_data.get(""),
        weight = pokemon_data.get(""),
        evolves_from_number = pokemon_data.get("")'''

#@app.get("/pokemon/{number}/scan")
#def pokemon(number:int):
    
