import secrets
import json

POKEMON = [
    {"name": "Pidgey", "id": 16, "gen": 1},
    {"name": "Spearow", "id": 21, "gen": 1},
    {"name": "Hoothoot", "id": 163, "gen": 2},
    {"name": "Taillow", "id": 276, "gen": 3},
    {"name": "Starly", "id": 396, "gen": 4},
    {"name": "Pidove", "id": 519, "gen": 5},
    {"name": "Fletchling", "id": 661, "gen": 6},
    {"name": "Pikipek", "id": 731, "gen": 7},
    {"name": "Rookidee", "id": 821, "gen": 8},
    {"name": "Wattrel", "id": 940, "gen": 9}
]


def get_birds_json():
    return json.dumps(POKEMON)


def choose_random_bird():
    return secrets.randbelow(len(POKEMON))
