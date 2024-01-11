import pygame


class Enemy_run(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('script/data/textures/enemy_run.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pos

        self.direction = pygame.math.Vector2(0, 0)

        self.a = 1
        self.life = True
        self.y = 0

    def update(self, x_shift, cos=False, death=False, up=False, down=False, down_down=False):
        if self.life:
            self.rect.x += x_shift + self.a
        if cos:
            if self.a == 1:
                self.a = -1
                self.rect.x += -4
            else:
                self.a = 1
                self.rect.x += 4
        if death:
            self.life = False
        if up:
            self.rect.y += -2
            self.y += 1
        if down:
            self.rect.y += 5
            self.y += 1
        if down_down:
            self.rect.y += 1000
            self.y += 1

