import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('script/data/textures/tnt.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift, explosion=False):
        self.rect.x += x_shift
        if explosion:
            self.image = pygame.image.load('script/data/textures/tnt2.png').convert_alpha()




