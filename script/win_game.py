import sys

import pygame


def win_game(screen):
    background = pygame.image.load('script/data/textures/win_g.png').convert_alpha()
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
        play_text = font.render("Return", True, (0, 0, 0))
        quit_text = font.render("Quit", True, (0, 0, 0))
        screen.blit(play_text, (play_button.x + 50, play_button.y + 10))
        screen.blit(quit_text, (quit_button.x + 50, quit_button.y + 10))

        pygame.display.update()
