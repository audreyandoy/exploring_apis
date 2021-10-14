from recipe import Recipe
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

def display_individual_recipe_info(recipes):
    for recipe in recipes:
        recipe_info = Recipe(recipe)
        recipe_info.display_title()
        recipe_info.display_ingredients()
        recipe_info.display_recipe_steps()

def main():
    recipes = get_recipe_list("Japanese", "vegetarian")
    display_individual_recipe_info(recipes)


if __name__ == "__main__":
    main()
