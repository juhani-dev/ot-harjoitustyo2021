import pygame
from ui import index

class Start():
    """luokka mikä luo aloitus ruudun mistä voi siirtyä itse peliin
    """
    def __init__(self):
        """luokan konstruktori
        Luo pygame ruudu annettujen parametrien mukaisesti
        """
        pygame.init()
        self.screen = pygame.display.set_mode([600, 600])
        pygame.display.set_caption("Start Screen")
        self.button = pygame.Rect(250, 250, 100, 100)
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        color = (255, 255, 255)
        self.text = self.smallfont.render('Start', True, color)
        self.loop()

    def loop(self):
        """Silmukka mikä tarkkailee tapahtumia ja piirtää pygame ruudun
        """
        while True:
            self.events()
            self.show_screen()

    def show_screen(self):
        """piirtää ruudulle napin mistä voi siirtyä peliin
        """
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, [255, 0, 0], self.button)
        self.screen.blit(self.text, (self.button.bottomleft, self.button.center))
        pygame.display.flip()

    def events(self):
        """tarkkailee mitä käyttäjä on hiirellään painanut
        """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.button.collidepoint(mouse_pos):
                    index.Blackjack()
            