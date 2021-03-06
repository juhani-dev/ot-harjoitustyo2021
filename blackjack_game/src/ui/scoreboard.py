import pygame
from services import check

class Scoreboard():
    """Luokka minkä avulla piirretään ruudulle pelaajan jä jakajan sen hetkisten
    korttien summa.
    """
    def __init__(self, player, dealer, screen):
        """luokan konstruktori
        Args:
            player :  lista missä pelaajan sen hetkiset kortit
            dealer :  lista missä jakajan sen hetkiset kortit
            screen : pygame ruutu mihin peli piirretään
        """
        self.player = player
        self.dealer = dealer
        self.screen = screen
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.color = (255, 255, 255)
        self.dealer_scoreboard = pygame.Rect(60, 400, 300, 70)
        self.player_scoreboard = pygame.Rect(360, 400, 300, 70)
    def scoreboard_dealer( self):
        """pirtää näytölle jakajan sen hetkisten korttien summan. Käyttää check tiedoston
        Checks luokkaa laskemiseen
        """
        pygame.draw.rect(self.screen, [10, 10, 10], self.dealer_scoreboard)
        score_dealer = str(check.Checks(self.player, self.dealer).count_dealer())
        score =  "dealer hand : "+score_dealer
        scoreboard_text = self.smallfont.render(score ,True, self.color)
        self.screen.blit(scoreboard_text, (60, 400))
    def scoreboard_player( self):
        """pirtää näytölle pelaajan sen hetkisten korttien summan. Käyttää check tiedoston
        Checks luokkaa laskemiseen
        """
        pygame.draw.rect(self.screen, [10, 10, 10], self.player_scoreboard)
        score_player = str(check.Checks(self.player, self.dealer).count_player())
        score =  "player hand : "+score_player
        scoreboard_text = self.smallfont.render(score ,True, self.color)
        self.screen.blit(scoreboard_text, (360, 400))
