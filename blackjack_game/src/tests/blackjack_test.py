import unittest
import ui.index
import pygame
import services.win_count as win_count
from services.check import Checks
from services.decks import CreateDeck

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

class TestWinCount(unittest.TestCase):
    def setUp(self):
        self.player = "player wins"
        self.count = win_count.Score(None).win_count(self.player)
    def test_player_wins(self):
        string = f"player wins: {1}  dealer wins: {0}"
        self.assertEqual(self.count,string)
