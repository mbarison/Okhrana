import random

from enum import Enum, IntEnum

random.seed(42)

class Seed(Enum):
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3
    CLUBS = 4
    RED = 5
    BLACK = 6

class Value(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    JOKER = 50

class Card:
    def __init__(self, seed, value):

        assert type(seed) == type(Seed(1))
        assert type(value) == type(Value(1))

        self._seed = seed
        self._value = value

    def __eq__(self, other):
        return self._seed == other._seed and self._value == other._value
    
    def __gt__(self, other):
        return self._value > other._value
    
    def __ge__(self, other):
        return self._value >= other._value

    def __lt__(self, other):
        return self._value < other._value  
    
    def __le__(self, other):
        return self._value <= other._value
    
def create_deck(jokers=True):
    deck = []

    for seed in range(1, 5):
        for value in range(1,14):
            deck.append(Card(Seed(seed), Value(value)))

    if jokers:
        for seed in range(5,7):
            deck.append(Card(Seed(seed), Value(50)))

    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def sort_deck(deck):
    return sorted(deck)

def deal_cards(deck, n=1):
    assert n > 0 and n <= len(deck)
    return (deck[:n], deck[n:])