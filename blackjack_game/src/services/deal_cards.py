from ast import literal_eval

from services import decks

class Deal():
    """Luokka luo pelin aloituksessa jaettavat kortit
    """
    def __init__(self):
        """Luokan konstruktori
        """
        self.player =[]
        self.dealer = []
    def start_position(self):
        """luo korttipakan decks tiedoston CreateDeck luokkaa käyttäen ja
        jakaa pelaajalle ja jakajalle aloitus kortit

        Returns:
            : pelaajan ja jakajan kortit
        """
        game_deck = decks.CreateDeck()
        self.cards = game_deck.get_deck()
        card = self.cards.pop()
        card = literal_eval(str(card)[1:-1])
        self.player.append(card)
        card = self.cards.pop()
        card = literal_eval(str(card)[1:-1])
        self.dealer.append(card)
        return self.player, self.dealer
    def player_hits(self):
        """lisää pelaajalle yhden kortin
        """
        card = self.cards.pop()
        card = literal_eval(str(card)[1:-1])
        self.player.append(card)
    def dealer_hits(self):
        """lisää jakajalle yhden kortin
        """
        card = self.cards.pop()
        card = literal_eval(str(card)[1:-1])
        self.dealer.append(card)
    def get_hands(self):
        """Palautus metodi

        Returns:
            palauttaa jakajan ja pelaajan kortit
        """
        return self.player, self.dealer
        