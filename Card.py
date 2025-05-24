from enum import Enum, IntEnum

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
    
    def get_seed(self):
        return self._seed

    def get_value(self):
        return self._value