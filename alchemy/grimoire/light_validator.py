from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = light_spellbook.light_spell_allowed_ingredients()
    for ingredient in valid_ingredients:
        if ingredient in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
