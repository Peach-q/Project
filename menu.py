import pygame
import sys

class Menu():
    back_game = pygame.image.load('images/space.png')

    def __init__(self, screen):
        self.screen = screen

    def update_menu(self):
        pygame.mouse.set_visible(False)

        font = pygame.font.Font('images/Fifaks10Dev1.ttf', 70)
        self.screen.blit(self.back_game, (0, 0))

        main_screen_word = font.render("Space rangers", 70, (255, 255, 255))
        self.screen.blit(main_screen_word, (140, 100))

        if 140 < pygame.mouse.get_pos()[0] < 460 and 380 < pygame.mouse.get_pos()[1] < 440:
            screen_word = font.render("Новая игра", True, (128, 0, 128))
        else:
            screen_word = font.render("Новая игра", True, (255, 255, 255))
        self.screen.blit(screen_word, (175, 380))

        if 180 < pygame.mouse.get_pos()[0] < 420 and 460 < pygame.mouse.get_pos()[1] < 520:
            screen_word = font.render("Выйти из игры", True, (128, 0, 128))
        else:
            screen_word = font.render("Выйти из игры", True, (255, 255, 255))
        self.screen.blit(screen_word, (140, 500))

        self.screen.blit(pygame.image.load('images/pixil-frame-0.png'), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        pygame.display.flip()
        pygame.display.update()

    def selection_from_the_menu(self):

        for game_event in pygame.event.get():
            if game_event.type == pygame.QUIT:
                sys.exit()
            if game_event.type == pygame.MOUSEBUTTONDOWN and game_event.button == 1:
                if 30 < pygame.mouse.get_pos()[0] < 400 and 400 < pygame.mouse.get_pos()[1] < 660:
                    sys.exit()
                return 100 < pygame.mouse.get_pos()[0] < 600 and 380 < pygame.mouse.get_pos()[1] < 440


        return False