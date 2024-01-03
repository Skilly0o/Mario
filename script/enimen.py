import pygame
from script.main_player import player



class Mob():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        # Логика движения моба

    def draw(self, screen):
        # Отрисовка моба на экране

    def check_collision(self, player):
        # Проверка столкновения с игроком

        if pygame.sprite.collide_rect(self, player):
            player.kill()