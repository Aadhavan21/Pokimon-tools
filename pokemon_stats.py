import json

POKEMON_STATS = {
    16: {"name": "Pidgey", "hp": 40, "attack": 45, "defense": 40, "sp_atk": 35, "sp_def": 35, "speed": 56, "total": 251},
    21: {"name": "Spearow", "hp": 40, "attack": 60, "defense": 30, "sp_atk": 31, "sp_def": 31, "speed": 70, "total": 262},
    163: {"name": "Hoothoot", "hp": 60, "attack": 30, "defense": 30, "sp_atk": 36, "sp_def": 56, "speed": 50, "total": 262},
    276: {"name": "Taillow", "hp": 40, "attack": 55, "defense": 30, "sp_atk": 30, "sp_def": 30, "speed": 85, "total": 270},
    396: {"name": "Starly", "hp": 40, "attack": 55, "defense": 30, "sp_atk": 30, "sp_def": 30, "speed": 60, "total": 245},
    519: {"name": "Pidove", "hp": 50, "attack": 55, "defense": 50, "sp_atk": 36, "sp_def": 30, "speed": 43, "total": 264},
    661: {"name": "Fletchling", "hp": 45, "attack": 50, "defense": 43, "sp_atk": 40, "sp_def": 38, "speed": 62, "total": 278},
    731: {"name": "Pikipek", "hp": 35, "attack": 75, "defense": 30, "sp_atk": 30, "sp_def": 30, "speed": 65, "total": 265},
    821: {"name": "Rookidee", "hp": 38, "attack": 47, "defense": 35, "sp_atk": 33, "sp_def": 35, "speed": 57, "total": 245},
    940: {"name": "Wattrel", "hp": 40, "attack": 40, "defense": 35, "sp_atk": 55, "sp_def": 40, "speed": 70, "total": 280}
}


def get_pokemon_stats(dex_id):
    dex_id = int(dex_id)
    if dex_id not in POKEMON_STATS:
        raise ValueError(f"Stats not found for Dex ID {dex_id}")
    return POKEMON_STATS[dex_id]


def get_pokemon_stats_json(dex_id):
    return json.dumps(get_pokemon_stats(dex_id))
