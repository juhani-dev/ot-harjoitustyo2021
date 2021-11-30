from typing import Text
import pygame
import random
class Blackjack():
    def __init__(self):
        pygame.init()
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
        self.start() 
        while True:
            self.events()
            
    
    def events(self):
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                exit()
            if action.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = action.pos  # gets mouse position
                if self.button.collidepoint(mouse_pos):
                    self.player_hit()
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
    def deal(self):
        self.eka = self.cards.pop()
        
        self.top = eval(str(self.eka)[1:-1])

        
        

    def show_card(self,x,y):
        self.card_eka =self.deal()
        self.card_eka =pygame.image.load(f"src/assets/cards_images/{self.top}")
        
        self.card_eka= pygame.transform.scale(self.card_eka, (100, 120))
        self.screen.blit(self.card_eka, (x,y))
        pygame.display.flip()

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
Blackjack()