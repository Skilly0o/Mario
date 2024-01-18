import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('script/data/textures/platform.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift, is_pause):
        if not is_pause:
            self.rect.x += x_shift


class Up_pipe(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('script/data/textures/truba.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
