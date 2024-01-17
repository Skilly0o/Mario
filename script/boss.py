import pygame
from script.player import Player

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

    def move(self):
        self.rect.x += self.speed
        self.jump()
        self.apply_gravity()

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
        self.direction.y = self.jump_speed


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def reverse_image(self):
        if self.speed > 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def update(self, shift):
        self.rect.x += shift
        self.move()
        self.reverse_image()
