# Перезапуск игры после проигрыша просто кликом мышки

import sys

import pygame

from script.game_over import game_over
from script.level import Level
from script.level_boss import Level_boss
from script.level_2 import Level_2
from script.menu import main_menu
from script.win_game import win_game
from script.setting import *

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

            background = pygame.image.load('script/data/textures/fon_2_lvl.jpg').convert_alpha()
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
                        level_2_go = False
                        level_1_go = False
                        level_3_go = True
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

        elif level_3_go:
            pygame.init()
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            background = pygame.image.load('script/data/textures/fon_3_lvl.jpg').convert_alpha()
            background = pygame.transform.smoothscale(background, screen.get_size())
            clock = pygame.time.Clock()
            level = Level_boss(boss_lvl, screen)
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
                        w_g = win_game(screen)
                        if w_g == 'play':
                            level.restart = False
                            level_3_go = False
                            level_1_go = True
                            exitt = False
                            break
                    if level.restart:
                        gover_menu = game_over(screen)
                        if gover_menu == 'play':
                            level.restart = False
                            level_3_go = False
                            level_1_go = True
                            exitt = False
                            break
                screen.blit(background, (0, 0))
                level.run()
                pygame.display.update()
                clock.tick(60)
