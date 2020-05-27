from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        self.name = str(name)
        now = datetime.now()
        self.last_update = now
        self.creation_date = now
        self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for meal_type in self.recipes_list:
            category = self.recipes_list[meal_type]
            recipe = next((r for r in category if r.name == name), None)
            if recipe:
                print(recipe)
                return recipe
        print(f"~{name}~ could not be found!")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        recipes = self.recipes_list.get(recipe_type)
        if recipes:
            print(f"Recipes from the {recipe_type} category:\n")
            print(*recipes, sep="\n\n")
        else:
            print(f"The {recipe_type} recipe type is empty or does not exist")
        return recipes

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if (isinstance(recipe, Recipe)):
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        else:
            raise TypeError(f"Recipe should be an instance of Recipe")
