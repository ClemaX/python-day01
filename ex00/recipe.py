class Recipe:
    def __init__(
            self,
            name,
            cooking_lvl,
            ingredients,
            description,
            recipe_type):
        if name and ingredients and recipe_type:
            self.name = str(name)
            self.cooking_lvl = int(cooking_lvl)
            if not 1 <= self.cooking_lvl <= 5:
                raise ValueError("Cooking level should be between 1 and 5")
            self.ingredients = list(str(i) for i in ingredients)
            self.recipe_type = str(recipe_type)
            self.description = str(description)
        else:
            raise ValueError("Only description of Recipe can be empty")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"~{self.name}~\n"
        txt += f"cooking level: {self.cooking_lvl} / 5\n"
        txt += "ingredients: \n"
        for ingredient in self.ingredients:
            txt += f" - {ingredient}\n"
        if self.description:
            txt += self.description + '\n'
        txt += f"To be eaten for {self.recipe_type}."
        return txt
