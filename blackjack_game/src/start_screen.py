import pygame
import index


class Start():
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode([600, 600])
        pygame.display.set_caption("Start Screen")
        self.button = pygame.Rect(250, 250, 100, 100)
        smallfont = pygame.font.SysFont('Corbel', 35)
        color = (255, 255, 255)

        self.text = smallfont.render('Start', True, color)
        self.loop()

    def loop(self):

        while True:
            self.events()
            self.show_screen()

    def show_screen(self):

        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, [255, 0, 0], self.button)
        self.screen.blit(
            self.text, (self.button.bottomleft, self.button.center))
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.button.collidepoint(mouse_pos):
                    index.Blackjack()
