
import pygame
from ui import game_screen, show
from services import deal_cards
from services import check
from services import check_winner
from services import win_count
from ui import show
from ui import game_screen
class Blackjack():
    """Luokka missä peliä pyörittävä silmukka sekä pygame ruudun ja nappien alustus
    """
    def __init__(self):
        """Luokan konstruktori
        """
        self.player = []
        self.dealer = []
        self.player_end = False
        self.dealer_end = False
        self.one_count = False
        self.screen = pygame.display.set_mode([1000, 600])

        self.game_screen = game_screen.Game_screen(self.screen)
        self.py_screen = self.game_screen.show_screen
        self.hit_button = pygame.Rect(500, 500, 70, 70)
        self.stop_button = pygame.Rect(300, 500, 70, 70)
        self.re_button = pygame.Rect(50, 500, 100, 70)
        #self.screen = pygame.display.set_mode([1000, 600])
        self.white = (255, 255, 255)
        self.font = pygame.font.SysFont('Corbel', 35)
        #pygame.display.set_caption("Blackjack")
        self.score = win_count.Score(self.screen)
        self.running()
    def running(self):
        """Peli silmukka
        """
        #self.show_screen()
        self.game_screen.show_screen()
        self.start = deal_cards.Deal()
        self.cards =self.start.start_position()
        show.Draw(self.screen).shows(self.cards[0],self.cards[1 ],self.score)
        while True:
            self.events()

    def events(self):
        """tarkkailee käyttäjän hiiren toimintaa
        """

        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                exit()
            if action.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = action.pos
                if self.hit_button.collidepoint(mouse_pos):
                    if check.Checks(self.cards[0],self.cards[1]).count_player() < 22 and self.player_end is False:
                        self.start.player_hits()
                        hit=self.start.get_hands()
                        show.Draw(self.screen).shows(hit[0],hit[1],self.score)
                if self.stop_button.collidepoint(mouse_pos):
                    self.player_end = True
                    hit = self.start.get_hands()
                    dealer_count = check.Checks(hit[0], hit[1]).count_dealer()
                    if len(self.dealer) < 2 and  self.dealer_end is False:
                        self.dealer_end = True
                        self.start.dealer_hits()
                        hit=self.start.get_hands()
                        show.Draw(self.screen).shows(hit[0],hit[1 ],self.score)
                    if  dealer_count < 16 and dealer_count < 18 :
                        while check.Checks(hit[0], hit[1]).count_dealer() < 16 and check.Checks(hit[0], hit[1]).count_dealer() < 18:
                            self.start.dealer_hits()
                            hit=self.start.get_hands()
                            show.Draw(self.screen).shows(hit[0],hit[1 ],self.score)
                    hit = self.start.get_hands()
                    final_player_hand = check.Checks(hit[0], hit[1]).count_player()
                    final_dealer_hand = check.Checks(hit[0], hit[1]).count_dealer()
                    winner = check_winner.Winner(final_player_hand,final_dealer_hand).get_winner()
                    winner_text = self.font.render(winner,True,self.white)
                    self.screen.blit(winner_text, (700, 250))
                    if self.one_count is False:
                        self.score.win_counter(winner)
                        self.one_count = True
                    self.score.win_count_draw()
                    pygame.display.flip()

                if self.re_button.collidepoint(mouse_pos) and self.dealer_end is True:
                    self.player_end = False
                    self.dealer_end = False
                    self.one_count = False
                    self.game_screen.show_screen()
                    #self.show_screen()
                    self.player = []
                    self.dealer = []
                    self.start = deal_cards.Deal()
                    self.cards =self.start.start_position()
                    show.Draw(self.screen).shows(self.cards[0],self.cards[1],self.score)
                    