import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from menu import Menu



def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption('Space rangers (Zenkevich home-project)')
    bg_color = (0, 0, 0)

    pygame.mixer.music.load('sound/сhill.wav')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    menu = Menu(screen)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)


    while True:
        if stats.run_game:
            controls.events(screen, gun, bullets)
            gun.update_gun()
            bullets.update()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)
        else:
            menu.update_menu()
            stats.run_game = menu.make_choice()

run()
