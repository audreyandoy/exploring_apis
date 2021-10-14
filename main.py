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

def display_title(recipe):
    print("="*40)
    print(f"             {recipe['title'].upper()}             ")
    print("="*40)

def display_ingredients(recipe):
    print("\nIngredients: ")
    print("------------")
    ingredients = recipe["extendedIngredients"]
    for ingredient in ingredients:
        print(ingredient["original"])

def display_recipe_steps(recipe):
    print("\nRecipe:")
    print("-------")
    recipe_steps = recipe["analyzedInstructions"][0]["steps"]
    for step in recipe_steps:
        print(f"#{step['number']} {step['step']} \n")

def main():
    recipes = get_recipe_list("Japanese", "vegetarian")

    for recipe in recipes:
        display_title(recipe)
        display_ingredients(recipe)
        display_recipe_steps(recipe)


if __name__ == "__main__":
    main()