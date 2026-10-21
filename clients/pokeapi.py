from fastapi import FastAPI
import requests


BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_from_api(pokemon_number: int):
    response = requests.get(
        BASE_URL + f"{pokemon_number}",
        timeout=10
    )
    response.raise_for_status()
    return response.json()

def get_species_from_api(species_url: str):
    response = requests.get(species_url, timeout=10)
    response.raise_for_status()
    return response.json()

def get_types_from_api(types_url: str):
    response = requests.get(types_url, timeout=10)
    response.raise_for_status()
    return response.json()


