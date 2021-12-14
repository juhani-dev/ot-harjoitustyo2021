import unittest
import ui.index
import pygame
from services.win_count import Score
from services.check import Checks
from services.decks import CreateDeck
import services.check_winner as check_win

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

class TestCheckWinner(unittest.TestCase):
    def setUp(self):
        pass
    def test_same_score(self):
        tester =check_win.Winner(20,20).get_winner()
        self.assertEqual(tester, "dealer wins")
    def test_same_score_21(self):
        tester =check_win.Winner(21,21).get_winner()
        self.assertEqual(tester, "draw")
    def test_player_under_dealer_over(self):
        tester =check_win.Winner(20,22).get_winner()
        self.assertEqual(tester, "player wins")
    def test_player_over_dealer_under(self):
        tester =check_win.Winner(22,20).get_winner()
        self.assertEqual(tester, "dealer wins")
    def test_player_jack(self):
        tester =check_win.Winner(21,19).get_winner()
        self.assertEqual(tester, "player wins")
    def test_dealer_jack(self):
        tester =check_win.Winner(19,21).get_winner()
        self.assertEqual(tester, "dealer wins")
    def test_both_under_player_wins(self):
        tester =check_win.Winner(19,18).get_winner()
        self.assertEqual(tester, "player wins")
    def test_both_under_dealer_wins(self):
        tester =check_win.Winner(18,19).get_winner()
        self.assertEqual(tester, "dealer wins")

class TestWinCount(unittest.TestCase):
    def setUp(self):
        self.player_count = 0
        self.dealer_count =  0
    def test_win_counter(self):
        winner = "dealer wins"
        output = f"player wins: {0}  dealer wins: {1}"
        tester = Score.win_counter(self,winner)
        self.assertEqual(tester, output)

    def test_win_counter_again(self):
        winner = "player wins"
        output = f"player wins: {1}  dealer wins: {0}"
        tester = Score.win_counter(self,winner)
        self.assertEqual(tester, output)