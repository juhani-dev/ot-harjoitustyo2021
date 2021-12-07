
import pygame
import decks
import check


class Blackjack():
    def __init__(self):
        self.player = []
        self.dealer = []
        self.player_end = False
        self.screen = pygame.display.set_mode([1000, 600])
        pygame.display.set_caption("Blackjack")
        self.running()

    def show_screen(self):
        self.screen.fill((10, 10, 10))
        self.hit_button = pygame.Rect(500, 500, 70, 70)
        self.stop_button = pygame.Rect(300, 500, 70, 70)
        self.re_button = pygame.Rect(50, 500, 100, 70)
        pygame.draw.rect(self.screen, [255, 0, 0], self.hit_button)
        pygame.draw.rect(self.screen, [255, 0, 0], self.stop_button)
        pygame.draw.rect(self.screen, [255, 0, 0], self.re_button)
        smallfont = pygame.font.SysFont('Corbel', 35)
        color = (255, 255, 255)
        self.text_hit = smallfont.render('hit', True, color)
        self.text_stop = smallfont.render('stop', True, color)
        self.text_re = smallfont.render('restart', True, color)
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
                    if check.Checks(self.player, self.dealer).count_player() < 22:
                        while check.Checks(self.player, self.dealer).count_dealer() < 16 and check.Checks(self.player, self.dealer).count_dealer() < 18:

                            self.dealer_hits()

                if self.re_button.collidepoint(mouse_pos):
                    self.player_end = False
                    self.show_screen()
                    self.player = []
                    self.dealer = []
                    self.game_start()
                    self.shows()

    def game_start(self):
        self.game_deck = decks.CreateDeck()

        self.cards = self.game_deck.get_deck()
        for i in range(1):
            card = self.cards.pop()
            card = eval(str(card)[1:-1])

            self.dealer.append(card)
            self.card = card

        card = self.cards.pop()
        card = eval(str(card)[1:-1])

        self.player.append(card)
        self.card = card

        print(self.player, "polayer")
        print(self.dealer, "dealer")

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
        pygame.display.flip()

    def player_hits(self):

        card = self.cards.pop()
        card = eval(str(card)[1:-1])
        self.player.append(card)
        self.shows()

    def dealer_hits(self):

        card = self.cards.pop()
        card = eval(str(card)[1:-1])
        self.dealer.append(card)
        self.shows()
