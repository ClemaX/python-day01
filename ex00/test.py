from book import Book
from recipe import Recipe

try:
    tourte = Recipe(
        "cake",
        3,
        ["eggs", "sugar", "oil", "meal", "yeast", "vanilla sugar"],
        """Preheat oven to 180°C.
Whisk everything up.
Cook at 180°C for ~35 min.""",
        'dessert'
    )

    sandwich = Recipe(
        "sandwich",
        2,
        ["ham", "bread", "cheese", "tomatoes"],
        "sudo make sandwich",
        'dessert'
    )

    book = Book("CookBook Pro")
    book.add_recipe(tourte)
    book.add_recipe(sandwich)
    book.get_recipes_by_types("dessert")
    print()
    book.get_recipe_by_name("cake")
except (ValueError, TypeError) as e:
    print("Error:", e)
