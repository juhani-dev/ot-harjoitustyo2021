
import pygame


import services.check as check
import services.decks as decks
import services.scoreboard as scoreboard
import services.check_winner as check_winner
import services.win_count as win_count
class Blackjack():
    def __init__(self):
        
        
        self.player = []
        self.dealer = []
        self.player_end = False
        self.screen = pygame.display.set_mode([1000, 600])
        self.white = (255, 255, 255)
        self.font = pygame.font.SysFont('Corbel', 35)
        pygame.display.set_caption("Blackjack")
        self.score = win_count.Score(self.screen)
        self.running()

    def show_screen(self):
        """piirtää pygame ruudulle napit mitä käyttäjä voi painaa
        """
        self.screen.fill((10, 10, 10))
        self.hit_button = pygame.Rect(500, 500, 70, 70)
        self.stop_button = pygame.Rect(300, 500, 70, 70)
        self.re_button = pygame.Rect(50, 500, 100, 70)
        pygame.draw.rect(self.screen, [255, 0, 0], self.hit_button)
        pygame.draw.rect(self.screen, [255, 0, 0], self.stop_button)
        pygame.draw.rect(self.screen, [255, 0, 0], self.re_button)
        self.text_hit = self.font.render('hit', True, self.white)
        self.text_stop = self.font.render('stop', True, self.white)
        self.text_re = self.font.render('restart', True, self.white)
        self.screen.blit(self.text_hit, (500, 500))
        self.screen.blit(self.text_stop, (300, 500))
        self.screen.blit(self.text_re, (50, 500))
        
        

        pygame.display.flip()

    def running(self):
        
        self.show_screen()
        self.game_start()
        self.shows()
        while True:

            self.events()

    def events(self):

        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                exit()
            if action.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = action.pos
                
                if self.hit_button.collidepoint(mouse_pos):
                    if check.Checks(self.player, self.dealer).count_player() < 22 and self.player_end is False:

                        self.player_hits()
                
                if self.stop_button.collidepoint(mouse_pos):
                    self.player_end = True
                    
                    player_count =check.Checks(self.player, self.dealer).count_player()
                    dealer_count = check.Checks(self.player, self.dealer).count_dealer()
                    if len(self.dealer) < 2:
                        self.dealer_hits()
                    if player_count < 22 and dealer_count < 16 and dealer_count < 18 :
                        
                        while check.Checks(self.player, self.dealer).count_dealer() < 16 and check.Checks(self.player, self.dealer).count_dealer() < 18:
                            
                            self.dealer_hits()
                    
                    final_player_hand = check.Checks(self.player, self.dealer).count_player()
                    final_dealer_hand = check.Checks(self.player, self.dealer).count_dealer()
                    winner = check_winner.Winner(final_player_hand,final_dealer_hand).get_winner()
                    self.winner_text = self.font.render(winner, True, self.white)
                    self.screen.blit(self.winner_text, (700, 250)) 

                    self.score.win_counter(winner)
                    self.score.win_count_draw()
                    pygame.display.flip()

                if self.re_button.collidepoint(mouse_pos):
                    self.player_end = False
                    self.show_screen()
                    self.player = []
                    self.dealer = []
                    self.game_start()
                    self.shows()

    def game_start(self):
        """Luo pelin ja jokaisen uuden käden aloitus tilanteen.
        luo pakan ja hakee pakan decks tiedoston CreateDeck luokan avulla.
        Lisää pelaajalle ja jakajalle yhdet kortit
        """
        self.game_deck = decks.CreateDeck()

        self.cards = self.game_deck.get_deck()
        for i in range(1):
            card = self.cards.pop()
            card = eval(str(card)[1:-1])
            self.dealer.append(card)
        card = self.cards.pop()
        card = eval(str(card)[1:-1])
        self.player.append(card)
        
    def shows(self):
        x = 100
        dy = 100
        py = 250
        for i in self.dealer:
            card = str(i[0])+i[1]
            x = x + 100
            i = pygame.image.load(f"src/assets/cards_images/{card}")
            a = pygame.transform.scale(i, (100, 120))
            self.screen.blit(a, (x, dy))
        x = 100
        for i in self.player:
            card = str(i[0])+i[1]
            x = x+100
            i = pygame.image.load(f"src/assets/cards_images/{card}")
            a = pygame.transform.scale(i, (100, 120))
            self.screen.blit(a, (x, py))
        self.score.win_counter("none")
        self.score.win_count_draw()
        scoreboard.Scoreboard(self.player,self.dealer,self.screen).scoreboard_dealer()
        scoreboard.Scoreboard(self.player,self.dealer,self.screen).scoreboard_player()
        pygame.display.flip()

    def player_hits(self):
        """lisää pelaajalle yhden kortin
        """

        card = self.cards.pop()
        card = eval(str(card)[1:-1])
        self.player.append(card)
        self.shows()

    def dealer_hits(self):
        """lisää jakajalle yhden kortin
        """

        card = self.cards.pop()
        card = eval(str(card)[1:-1])
        self.dealer.append(card)
        self.shows()
