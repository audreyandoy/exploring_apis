import requests


def get_recipe_list(cuisine, diet):
    PATH = "https://api.spoonacular.com/recipes/complexSearch"
    API_KEY = "078202005f0c4419b280d63f1f5f4ca8"

    query_params = {
        "cuisine": cuisine,
        "diet": diet,
        "addRecipeInformation": True,
        "fillIngredients": True,
        "apiKey": API_KEY
    }
    response = requests.get(PATH, params=query_params)
    return response.json()["results"]


import requests

def get_recipe_list(cuisine, diet):
    PATH = "https://api.spoonacular.com/recipes/complexSearch"
    API_KEY = "078202005f0c4419b280d63f1f5f4ca8"

    query_params = {
        "cuisine": cuisine,
        "diet": diet,
        "addRecipeInformation": True,
        "fillIngredients": True, 
        "apiKey": API_KEY 
    }
    response = requests.get(PATH, params = query_params)
    return response.json()["results"]

# get all recipes
recipes = get_recipe_list("Japanese", "vegetarian")

# get individual recipes
for recipe in recipes:
    print("="*40)
    print(f"             {recipe['title'].upper()}             ")
    print("="*40)

    # get individual ingredients
    print("\nIngredients: ")
    print("------------")
    ingredients = recipe["extendedIngredients"]
    for ingredient in ingredients:
        print(ingredient["original"])
    
    # get individual recipe steps
    print("\nRecipe:")
    print("-------")
    recipe_steps = recipe["analyzedInstructions"][0]["steps"]
    for step in recipe_steps:
        print(f"#{step['number']} {step['step']} \n")

