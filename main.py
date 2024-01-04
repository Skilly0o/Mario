import pygame
import sys
from script.setting import *
from script.level import Level


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
level = Level(level_map, screen)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('purple')
    level.run()

    pygame.display.update()
    clock.tick(60)