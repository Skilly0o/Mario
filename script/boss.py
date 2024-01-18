import time

import pygame


class Boss(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('script/data/textures/boss.png').convert_alpha()

        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)

        self.gravity = 0.8
        self.jump_speed = -16

        self.health = 3
        self.speed = 6

        self.last_jump_time = time.time()

    def move(self, is_pause3):
        if not is_pause3:
            self.rect.x += self.speed
            self.jump()

    def damage(self):
        self.health -= 1
        print(self.health)
        if self.health <= 0:
            self.kill()
        elif self.health == 2:
            self.speed = 8
        elif self.health == 1:
            self.speed = 10

    def jump(self):
        current_time = time.time()
        if current_time - self.last_jump_time >= 3:
            self.direction.y = self.jump_speed
            self.last_jump_time = current_time

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def update(self, shift, is_pause3):
        self.rect.x += shift
        self.move(is_pause3)
        self.reverse_image()
