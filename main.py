# Перезапуск игры после проигрыша просто кликом мышки

import pygame
import sys
from script.setting import *
from script.level import Level
from script.level_2 import Level_2
from script.menu import main_menu
from script.game_over import game_over


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

menu_choice = main_menu(screen)

level_1_go = True
level_2_go = False
level_3_go = False


exitt = True
if menu_choice == "play":
    while True:
        exitt = True
        if level_1_go:
            pygame.init()
            screen = pygame.display.set_mode((WIDTH, HEIGHT))

            background = pygame.image.load('script/data/textures/fon.jpg').convert_alpha()
            background = pygame.transform.smoothscale(background, screen.get_size())

            clock = pygame.time.Clock()

            level = Level(level_map, screen)

            while exitt:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if level.end_level:
                        level_2_go = True
                        level_1_go = False
                        exitt = False

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

        elif level_2_go:
            pygame.init()
            screen = pygame.display.set_mode((WIDTH, HEIGHT))

            background = pygame.image.load('script/data/textures/fon.jpg').convert_alpha()
            background = pygame.transform.smoothscale(background, screen.get_size())

            clock = pygame.time.Clock()

            level = Level_2(level_2_map, screen)

            while exitt:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()


                    if level.end_level:
                        level_2_go = True
                        level_1_go = False
                        exitt = False

                    if level.restart:
                        gover_menu = game_over(screen)
                        if gover_menu == 'play':
                            level.restart = False
                            level_2_go = False
                            level_1_go = True
                            exitt = False
                            break

                screen.blit(background, (0, 0))
                level.run()
                pygame.display.update()
                clock.tick(60)