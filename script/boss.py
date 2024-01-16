import pygame
import random
from script.setting import WIDTH, HEIGHT



class Boss(pygame.sprite.Sprite):
    def __init__(self, player, pos):
        super().__init__()
        self.image = pygame.image.load('script/data/textures/test.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.player = player

    def update(self):
        player_pos = self.player.rect.center
        boss_pos = self.rect.center

        dx = player_pos[0] - boss_pos[0]
        dy = player_pos[1] - boss_pos[1]

        length = (dx ** 2 + dy ** 2) ** 0.5
        if length != 0:
            dx /= length
            dy /= length

        speed = 3
        self.rect.x += dx * speed
        self.rect.y += dy * speed

        if self.rect.right > WIDTH:
            self.rect.left = 0
        elif self.rect.left < 0:
            self.rect.right = WIDTH

        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
        elif self.rect.top < 0:
            self.rect.bottom = HEIGHT