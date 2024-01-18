import os

import pygame
from camera import Camera, screen_height

os.chdir('D:\python\my_projects\pygame_mario')  # Тут пропишите путь вашего раб каталога что бы питон мог исать папки
# для наглядности попробуйде удалить строку выше вам выдаст ошибку
pygame.init()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

black = (0, 0, 0)
white = (255, 255, 255)


# Класс главного героя
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load(f"data/textures/test.png").convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = screen_height - 100
        self.vel_x = 0
        self.vel_y = 0
        self.is_jumping = False
        self.jump_height = -16

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Гравитация
        if self.rect.y < screen_height - 50:
            self.vel_y += 0.5
        else:
            self.vel_y = 0
            self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.vel_y = self.jump_height
            self.is_jumping = True

    def move_left(self):
        self.vel_x = -3
        self.image = pygame.transform.flip(self.original_image, True, False)

    def move_right(self):
        self.vel_x = 3
        self.image = self.original_image

    def stop(self):
        self.vel_x = 0

    def update_position(self):
        if pygame.key.get_pressed()[pygame.K_UP]:
            player.jump()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            player.move_left()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            player.move_right()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()


all_sprites = pygame.sprite.Group()

player = Player()
camera = Camera()
all_sprites.add(player)
clock = pygame.time.Clock()
# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    player.update_position()
    all_sprites.update()
    screen.fill((0, 0, 200))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()