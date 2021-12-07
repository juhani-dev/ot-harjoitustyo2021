import unittest
from check import Checks
from decks import CreateDeck

deck = [(8, "RU.png"), (9, "RU.png")]
deck2 = [(10, "RU.png"), (7, "RU.png"), (2, "RU.png")]


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.cards = CreateDeck()

    def test_cards52(self):
        deck = self.cards.get_deck()

        self.assertEqual(len(deck), 52)


class TestCheck(unittest.TestCase):
    def setUp(self):
        self.deck = Checks(deck, deck2)

    def test_player_hand_size(self):
        hand = self.deck.count_player()

        self.assertEqual(hand, 17)

    def test_dealer_hand_size(self):
        hand = self.deck.count_dealer()

        self.assertEqual(hand, 19)
