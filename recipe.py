class Recipe:
    def __init__(self, data):
        self.data = data

    def display_title(self):
        print("="*len(self.data['title']))
        print(f"{self.data['title'].upper()}")
        print("="*len(self.data['title']))


    def display_ingredients(self):
        print("\nIngredients: ")
        print("------------")
        ingredients = self.data["extendedIngredients"]
        for ingredient in ingredients:
            print(ingredient["original"])

    def display_recipe_steps(self):
        print("\nRecipe:")
        print("-------")
        recipe_steps = self.data["analyzedInstructions"][0]["steps"]
        for step in recipe_steps:
            print(f"#{step['number']} {step['step']} \n")


 