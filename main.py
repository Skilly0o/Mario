import pygame
import sys

from script.game_over import game_over
from script.level import *
from script.level_2 import Level_2
from script.level_boss import Level_boss
from script.menu import main_menu
from script.setting import *
from script.win_game import win_game

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

menu_choice = main_menu(screen)

level_1_go = True
level_2_go = False
level_3_go = False

is_pause1 = False
is_pause2 = False
is_pause3 = False

exitt = True
count = 0

pause_button = pygame.Rect(WIDTH - 150, 0, 150, 50)
font = pygame.font.Font(None, 36)
pause_text = font.render("Pause", True, "black")

if menu_choice == "play":
    while True:
        exitt = True
        if level_1_go:
            count += 1
            pygame.init()
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            background = pygame.image.load('script/data/textures/fon.jpg').convert_alpha()
            background = pygame.transform.smoothscale(background, screen.get_size())

            clock = pygame.time.Clock()

            level = Level(level_map, screen)

            while exitt:
                for event in pygame.event.get():
                    mouse_pos = pygame.mouse.get_pos()
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
                    if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN
                                                                and event.key == pygame.K_ESCAPE):
                        if pause_button.collidepoint(mouse_pos) or (event.type == pygame.KEYDOWN
                                                                    and event.key == pygame.K_ESCAPE):
                            is_pause1 = not is_pause1
                        if continue_button.collidepoint(mouse_pos):
                            if is_pause1:
                                is_pause1 = not is_pause1
                        if quit_button.collidepoint(mouse_pos):
                            if is_pause1:
                                exitt = False
                                is_pause1 = not is_pause1
                                pygame.quit()
                                sys.exit()
                screen.blit(background, (0, 0))
                level.run(is_pause1, count)
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
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
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

                    if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN
                                                                and event.key == pygame.K_ESCAPE):
                        if pause_button.collidepoint(mouse_pos) or (event.type == pygame.KEYDOWN
                                                                    and event.key == pygame.K_ESCAPE):
                            is_pause2 = not is_pause2
                        if continue_button.collidepoint(mouse_pos):
                            if is_pause2:
                                is_pause2 = not is_pause2
                        if quit_button.collidepoint(mouse_pos):
                            if is_pause2:
                                exitt = False
                                is_pause2 = not is_pause2
                                pygame.quit()
                                sys.exit()

                screen.blit(background, (0, 0))
                level.run(is_pause2)
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
                    mouse_pos = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
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

                    if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN
                                                                and event.key == pygame.K_ESCAPE):
                        if pause_button.collidepoint(mouse_pos) or (event.type == pygame.KEYDOWN
                                                                    and event.key == pygame.K_ESCAPE):
                            is_pause3 = not is_pause3
                        if continue_button.collidepoint(mouse_pos):
                            if is_pause3:
                                is_pause3 = not is_pause3
                        if quit_button.collidepoint(mouse_pos):
                            if is_pause3:
                                exitt = False
                                is_pause3 = not is_pause3
                                pygame.quit()
                                sys.exit()
                screen.blit(background, (0, 0))
                level.run(is_pause3)
                pygame.display.update()
                clock.tick(60)
