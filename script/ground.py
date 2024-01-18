import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('script/data/textures/ground.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift, is_pause=False):
        self.rect.x += x_shift


class Pipe(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('script/data/textures/truba_2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift