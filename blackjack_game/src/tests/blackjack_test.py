
import unittest
from services.win_count import Score
from services.check import Checks
from services.decks import CreateDeck
import services.check_winner as check_win
from services import deal_cards

deck1 = [(8, "RU.png"), (9, "RU.png")]
deck2 = [(10, "RU.png"), (7, "RU.png"), (2, "RU.png")]
ace_deck = [(8, "RU.png"), (14, "RU.png")]

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = CreateDeck()
        self.deck2 = CreateDeck()
        self.cards = self.deck.get_deck()
        self.cards2 = self.deck2.get_deck()
    def test_cards52(self):

        self.assertEqual(len(self.cards), 52)
    def test_suits(self):
        counter = 0
        for i in self.cards:
            if str(i[1]) == "HE.png":
                counter = counter +1
        self.assertEqual(counter, 13)
    def test_values(self):
        counter = 0
        for i in self.cards:
            if int(i[0]) == 8:
                counter = counter +1
        self.assertEqual(counter,4)
    def test_shuffle(self):
        self.assertTrue(self.cards, self.cards2)
class TestCheck(unittest.TestCase):
    def setUp(self):
        self.deck = Checks(deck1, deck2)
        self.deck_with_ace = Checks(ace_deck, deck2)

    def test_player_hand_size(self):
        hand = self.deck.count_player()
        self.assertEqual(hand, 17)

    def test_dealer_hand_size(self):
        hand = self.deck.count_dealer()
        self.assertEqual(hand, 19)

    def test_ace_count(self):
        hand = self.deck_with_ace.count_player()
        self.assertEqual(hand, 9)

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

class TestDealCards(unittest.TestCase):
    def setUp(self):
        self.tester  = deal_cards.Deal()

    def test_constructor(self):
        hands =self.tester.get_hands()
        self.assertEqual(len(hands[0]),0)

    def test_start_position(self):
        self.tester.start_position()
        hands =self.tester.get_hands()
        self.assertEqual(len(hands[0]),1)
    def test_player_hits(self):
        self.tester.start_position()
        self.tester.player_hits()
        self.tester.player_hits()
        cards = self.tester.get_hands()
        self.assertEqual(len(cards[0]),3)

    def test_dealer_hits(self):
        self.tester.start_position()
        self.tester.dealer_hits()
        self.tester.dealer_hits()
        self.tester.dealer_hits()
        cards = self.tester.get_hands()
        self.assertEqual(len(cards[1]),4)
