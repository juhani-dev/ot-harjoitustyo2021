import pygame
class Score():
    """Luokka mikä laskee  kuinka monta peliä jakaja ja pelaaja ovat voittaneet.  
    Piirtää myös tuloksen ruudulle
    """
    def __init__(self,screen):
        """Luokan konstruktori. Luo pelaajan ja jakajan voittojen määristä kirjaa pitävät muuttujat.


        Args:
            screen : pygame:issa luotu näyttö
        """
        self.player_count = 0
        self.dealer_count = 0
        self.screen = screen
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.color = (255, 255, 255)
    def win_count(self,winner):
        """ Lisää voitoista kirjaa pitäviin muuttujiin yhden rippuen voittajasta
            Luo tekstin (self.result) missä näkee voittojen määrän
        Args:
            winner : check_winner tiedoston Winner luokan avulla luotu string mikä kertoo 
            pelatun käden voittajan
        """
        if winner == "dealer wins":        
            self.dealer_count =self.dealer_count +1
        if winner == "player wins":
            self.player_count =self.player_count +1   
        self.result = f"player wins: {self.player_count}  dealer wins: {self.dealer_count}"
        
        return self.result
    def win_count_draw(self):
        """Piirtää ruudulle tekstin mikä kertoo käyttäjälle voittojen määrän
        """
        score = pygame.Rect(50, 50, 500, 40)
        self.draw =pygame.draw.rect(self.screen, [10, 10, 10], score)  
        self.scoreboard_text = self.smallfont.render(self.result ,True, self.color)
        self.screen.blit(self.scoreboard_text, (50, 50))