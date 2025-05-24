import random

random.seed(42)

from Card import Card, Seed, Value
from Hand import Hand

class Deck:
    def __init__(self, jokers=False):
        self._cards = []

        for seed in range(1, 5):
            for value in range(1,14):
                self._cards.append(Card(Seed(seed), Value(value)))

        if jokers:
            for seed in range(5,7):
                self._cards.append(Card(Seed(seed), Value(50)))

    def shuffle(self):
        random.shuffle(self._cards)

    def sort(self):
        self._cards = sorted(self._cards)

    def deal_cards(self, n=1):
        assert n > 0 and n <= len(self._cards)
        hand = Hand(self._cards[:n])
        self._cards = self._cards[n:]
        return hand    