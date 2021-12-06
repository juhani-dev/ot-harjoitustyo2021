from typing import Text
import pygame
import random
import start_screen
import Decks

import test
class Blackjack():
    def __init__(self):
        self.player =[]
        self.dealer =[]
       
        self.game_deck= Decks.Create_Deck()
        self.aa =self.game_deck.get_deck()
        print(self.aa)
        
        self.screen = pygame.display.set_mode([1000, 600])
        self.button = pygame.Rect(500, 500, 50, 50)
        smallfont = pygame.font.SysFont('Corbel',35)
        color=(255,255,255)  

        self.text = smallfont.render('hit' , True , color)
        pygame.display.set_caption("Blackjacks")

        self.show_screen()
        self.deck_of_cards()
        
        self.running()
    

    
    def show_screen(self):
        self.screen.fill((10,10,10))
        pygame.draw.rect(self.screen, [255, 0, 0], self.button)
        
        self.screen.blit(self.text , (500,500))
        pygame.display.flip()
    
    def running(self):
     
        self.game_start()
        self.shows()
        self.count_player()
        self.count_dealer()
        print(self.player,"player")
        print(self.dealer,"dealer")
        while True:
            self.events()
            
    
    def events(self):
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                exit()
            if action.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = action.pos 
                if self.button.collidepoint(mouse_pos):
                    self.player_hits()
                    print('button was pressed at {0}'.format(mouse_pos))

    
    def deck_of_cards(self):
        self.cards =[]
        self.maat= ["PA","HE","RU","RI"]
        for i in range(2,14):
            for j in self.maat:
                i = str(i)
                self.cards.append([i+j+".png"])
        random.shuffle(self.cards)

        return self.cards

    
    def start(self):
        
        x = 0
        y = 100
        for i in range(3):
            x =  x+100
            if i == 2:
                x =100
                y =300
            self.show_card(x,y)
            
    def player_hit(self):
        self.show_card(200,300)

    def game_start(self):
        for i in range(2):
            j = self.aa.pop()
            j=eval(str(j)[1:-1])
            
            self.dealer.append(j)
            self.j =j
            
        
        j = self.aa.pop()
        j=eval(str(j)[1:-1])
        
        self.player.append(j)
        self.j = j
        
        print(self.player,"polayer")
        print(self.dealer,"dealer")

    def shows(self):
        x= 100 
        dy = 100
        py= 250
        for i in self.dealer:
            
            card = str(i[0])+i[1]
            x = x +100
            i =pygame.image.load(f"assets/cards_images/{card}")
            a= pygame.transform.scale(i, (100, 120))

            self.screen.blit(a, (x,dy))
        x=100

        for i in self.player:
            card = str(i[0])+i[1]
            x=x+100
            i =pygame.image.load(f"assets/cards_images/{card}")
        
            a= pygame.transform.scale(i, (100, 120))

            self.screen.blit(a, (x,py))

        pygame.display.flip()
    
    def player_hits(self):

        j = self.aa.pop()
        j=eval(str(j)[1:-1])
        
        self.player.append(j)

        self.shows()
    def dealer_hits(self):

        j = self.aa.pop()
        j=eval(str(j)[1:-1])
        
        self.dealer.append(j)

        self.shows()
    
    def count_player(self):
        count = 0
        for i in self.player:
            count=count+int(i[0])
            
        

    def count_dealer(self):
        count = 0
        for i in self.dealer:
            count=count+int(i[0])
            
        