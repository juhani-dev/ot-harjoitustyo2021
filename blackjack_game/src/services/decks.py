import random


class CreateDeck():
    """ Luokka joka luo korttipakan
    """
    def __init__(self):
        """ luokan konstruktori joka luo tyhjän korttipakan lista muodossa
        """
        self.cards = []
        self.deck_of_cards()

    def deck_of_cards(self):
        """Lisää listamuotoiseen korttipakkaan korrtien arvot, maat ja sekoittaa järjestyksen

        """
        self.maat = ["PA", "HE", "RU", "RI"]
        for i in range(2, 15):
            for j in self.maat:
                i = str(i)
                self.cards.append([i, j+".png"])
        random.shuffle(self.cards)

    def get_deck(self):
        """palauttaa korttipakan

        Returns:
            : palauttaa korrtipakan
        """
        return self.cards
