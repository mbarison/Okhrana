from Card import Card, Seed, Value

class Hand:
    def __init__(self, cards = []):
        self._cards = cards

    def get_cards(self):
        return self._cards

    def sum(self):
        return sum([i.get_value() for i in self._cards])

    def add_cards(self, h):
        self._cards = self._cards + h.get_cards()

    def count_cards(self):
        return len(self._cards)

    def __add__(self, h):
        return self.get_cards() + h.get_cards()