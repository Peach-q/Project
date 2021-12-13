import pygame
import sys
class Menu():
    back_game = pygame.image.load('images/space.png')
    def __init__(self, screen):
        self.screen = screen

    def update_menu(self):
        pygame.mouse.set_visible(False)

        main_font = pygame.font.Font('images/Datcub.ttf', 85)
        font = pygame.font.Font('images/Fifaks10Dev1.ttf', 70)
        self.screen.blit(self.back_game, (0, 0))

        main_screen_word = main_font.render("Space rangers", 70, (255, 255, 255))
        self.screen.blit(main_screen_word, (55, 100))
        if 150 < pygame.mouse.get_pos()[0] < 470 and 390 < pygame.mouse.get_pos()[1] < 450:
            text = font.render("Новая игра", True, (128, 0, 128))
        else:
            text = font.render("Новая игра", True, (255, 255, 255))
        self.screen.blit(text, (140, 380))
        if 200 < pygame.mouse.get_pos()[0] < 410 and 470 < pygame.mouse.get_pos()[1] < 530:
            text = font.render("Выход", True, (128, 0, 128))
        else:
            text = font.render("Выход", True, (255, 255, 255))
        self.screen.blit(text, (200, 470))
        self.screen.blit(pygame.image.load('images/pixil-frame-0.png'), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        pygame.display.flip()
        pygame.display.update()


    def selection_from_the_menu(self):

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                if 200 < pygame.mouse.get_pos()[0] < 400 and 460 < pygame.mouse.get_pos()[1] < 520:
                    sys.exit()
                return 150 < pygame.mouse.get_pos()[0] < 470 and 390 < pygame.mouse.get_pos()[1] < 450
            
        return False
