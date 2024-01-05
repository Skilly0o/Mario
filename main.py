import pygame
import sys
from script.setting import *
from script.level import Level


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load('script/data/textures/fon.jpg').convert_alpha()
background = pygame.transform.smoothscale(background, screen.get_size())
clock = pygame.time.Clock()
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    level.run()

    pygame.display.update()
    clock.tick(60)