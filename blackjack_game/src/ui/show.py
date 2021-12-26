import pygame
from ui import scoreboard

class Draw():
    """Luokka mikä piirtää peli ikkunaan kortit
    """
    def __init__(self,screen):
        """konstruktori

        Args:
            screen : pygame ikkuna
        """
        self.screen = screen
    def shows(self,player, dealer, score):
        """Hakee pelaajan ja jakajan kortteja vastaavat kuvat tiedostosta ja piirtää ne 
        peli ikkunaan.

        Args:
            player : pelaajan kortit
            dealer : jakajan kortit
            score  : voittojen määrä 
        """
        self.player =player
        self.dealer = dealer
        self.score = score
        x_axel = 100
        dealer_y = 100
        player_y = 250
        for i in self.dealer:
            card = str(i[0])+i[1]
            x_axel = x_axel + 100
            image = pygame.image.load(f"src/assets/cards_images/{card}")
            image_a = pygame.transform.scale(image, (100, 120))
            self.screen.blit(image_a, (x_axel, dealer_y))
        x_axel = 100
        for i in self.player:
            card = str(i[0])+i[1]
            x_axel = x_axel+100
            image = pygame.image.load(f"src/assets/cards_images/{card}")
            image_a = pygame.transform.scale(image, (100, 120))
            self.screen.blit(image_a, (x_axel, player_y))
        self.score.win_counter("none")
        self.score.win_count_draw()
        scoreboard.Scoreboard(self.player,self.dealer,self.screen).scoreboard_dealer()
        scoreboard.Scoreboard(self.player,self.dealer,self.screen).scoreboard_player()
        pygame.display.flip()
        