import random
import index
import pygame
class Create_Deck():
    def __init__(self):
        self.cards =[]
        self.deck_of_cards()
    def deck_of_cards(self):
        self.maat= ["PA","HE","RU","RI"]
        for i in range(2,15):
            for j in self.maat:
                i = str(i)
                self.cards.append([i,j+".png"])
        random.shuffle(self.cards)

    def get_deck(self):
        return self.cards
        