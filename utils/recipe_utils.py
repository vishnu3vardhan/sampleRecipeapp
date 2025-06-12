import json

def load_recipes(filepath="recipes/recipes.json"):
    with open(filepath, 'r') as f:
        return json.load(f)

def save_recipes(recipes, filepath="recipes/recipes.json"):
    with open(filepath, 'w') as f:
        json.dump(recipes, f, indent=2)
