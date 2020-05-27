class GotCharacter:
    """A class representing a GoT family."""
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    """A class representing the Stark family."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """Print this family's house words"""
        print(self.house_words)

    def die(self):
        """There's nothing else to do."""
        self.is_alive = False
