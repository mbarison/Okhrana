from Card import Seed, Value
from Hand import Hand

class Requirement:
    def __init__(self, points=0, seeds=[Seed.SPADES, Seed.HEARTS, Seed.DIAMONDS, Seed.CLUBS]):
        self._req_points = points
        self._req_seeds = seeds

    def pass_req(self, hand):
        good_cards = Hand(list(filter(lambda x: x.get_seed() in self._req_seeds, hand.get_cards())))

        return good_cards.sum() >= self._req_points