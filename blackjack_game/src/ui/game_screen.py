import pygame
from services import win_count
class Game_screen():
    """Luokka mikä piirtää  peli ikkunan ja napit
    """
    def __init__(self,screen):
        """konstuktori

        Args:
            screen: pygame ikkuna
        """
        self.hit_button = pygame.Rect(500, 500, 70, 70)
        self.stop_button = pygame.Rect(300, 500, 70, 70)
        self.re_button = pygame.Rect(50, 500, 100, 70)
        self.screen = screen
        self.white = (255, 255, 255)
        self.font = pygame.font.SysFont('Corbel', 35)
        pygame.display.set_caption("Blackjack")
        self.score = win_count.Score(self.screen)
    def show_screen(self):
        """piirtää pygame ruudulle napit mitä käyttäjä voi painaa
        """
        self.screen.fill((10, 10, 10))
        pygame.draw.rect(self.screen, [255, 0, 0], self.hit_button)
        pygame.draw.rect(self.screen, [255, 0, 0], self.stop_button)
        pygame.draw.rect(self.screen, [255, 0, 0], self.re_button)
        text_hit = self.font.render('hit', True, self.white)
        text_stop = self.font.render('stop', True, self.white)
        text_re = self.font.render('restart', True, self.white)
        self.screen.blit(text_hit, (500, 500))
        self.screen.blit(text_stop, (300, 500))
        self.screen.blit(text_re, (50, 500))
        pygame.display.flip()