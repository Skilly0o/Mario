
import sys
from math import sin, pi

import pygame

def main_menu(screen):
    background = pygame.image.load('script/data/textures/main_menu.jpg').convert_alpha()
    background = pygame.transform.smoothscale(background, screen.get_size())

    play_button = pygame.Rect(50, 200, 200, 50)
    quit_button = pygame.Rect(50, 300, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    return "play"
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(background, (0, 0))

        pygame.draw.rect(screen, (0, 255, 0), play_button)
        pygame.draw.rect(screen, (255, 0, 0), quit_button)

        font = pygame.font.Font(None, 36)

        play_text = font.render("Play", True, (0, 0, 0))
        quit_text = font.render("Quit", True, (0, 0, 0))

        # Расположение кнопок
        screen.blit(play_text, (play_button.x + 50, play_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 50, quit_button.y + 10))

        # Расположение текста "2077" по середине экрана
        font_size = 48  # Увеличенный размер текста

        # Начальные значения для эффекта мерцания
        start_time = pygame.time.get_ticks()
        flicker_interval = 1000  # Интервал мерцания в миллисекундах
        flicker_color = (255, 0, 0)

        elapsed_time = pygame.time.get_ticks() - start_time
        flicker_factor = 0.5 + 0.5 * sin(2 * pi * elapsed_time / flicker_interval)
        flicker_color_effect = (
            int(flicker_color[0] * flicker_factor),
            int(flicker_color[1] * flicker_factor),
            int(flicker_color[2] * flicker_factor),
        )

        font = pygame.font.Font(None, 100)

        text = font.render("2077", True, flicker_color_effect)
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)

        pygame.display.update()

