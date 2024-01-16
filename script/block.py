import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('script/data/textures/block.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.wall = True
        self.life = True

    def update(self, x_shift, cos=False, down=False):
        if cos:
            self.wall = False
        if down:
            self.rect.y += x_shift
        else:
            self.rect.x += x_shift