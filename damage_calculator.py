import random
import json


def calculate_damage(L, P, A, D, stab, effectiveness, critical):

    if L <= 0 or P <= 0 or A <= 0 or D <= 0:
        raise ValueError("All stats must be greater than zero.")

    # Base damage formula (Generation 3)
    base_damage = (
        ((2 * L / 5 + 2) * P * A / D) / 50
    ) + 2

    # Apply modifiers
    modifier = stab * effectiveness * critical

    # Random damage factor (85% to 100%)
    damage = int(
        base_damage * modifier * random.randint(85, 100) / 100
    )

    return max(1, damage)


def calculate_damage_results(L, P, A, D, stab, effectiveness, critical):

    damages = [
        calculate_damage(
            L, P, A, D,
            stab, effectiveness, critical
        )
        for _ in range(1000)
    ]

    return {
        "minimum": min(damages),
        "maximum": max(damages),
        "average": round(sum(damages) / len(damages), 2)
    }


def calculate_damage_results_json(L, P, A, D, stab, effectiveness, critical):

    results = calculate_damage_results(
        L, P, A, D,
        stab, effectiveness, critical
    )

    return json.dumps(results)
