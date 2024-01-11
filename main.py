# Перезапуск игры после проигрыша просто кликом мышки

import pygame
import sys
from script.setting import *
from script.level import Level
from script.menu import main_menu
from script.game_over import game_over


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

menu_choice = main_menu(screen)



exitt = True
if menu_choice == "play":
    while True:
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        background = pygame.image.load('script/data/textures/fon.jpg').convert_alpha()
        background = pygame.transform.smoothscale(background, screen.get_size())

        clock = pygame.time.Clock()

        level = Level(level_map, screen)
        exitt = True

        while exitt:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if level.restart:
                    gover_menu = game_over(screen)
                    if gover_menu == 'play':
                        level.restart = False
                        exitt = False
                        break
            screen.blit(background, (0, 0))
            level.run()
            pygame.display.update()
            clock.tick(60)