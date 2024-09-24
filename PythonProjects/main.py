import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = ''
TRAINER_ID = ''
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Big boy",
    "photo_id": 1
}

response_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.json())

body_changename = {
    "pokemon_id": "",
    "name": "little boy",
    "photo_id": 1
}

response_changename = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_changename)
print(response_changename.json())

body_pokeball = {
    "pokemon_id": ""
}

response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokeball)
print(response_pokeball.json())