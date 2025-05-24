from Card import Card, Seed, Value

class Hand:
    def __init__(self, cards = []):
        self._cards = cards

    def get_cards(self):
        return self._cards

    def sum(self):
        return sum([i.get_value() for i in self._cards])