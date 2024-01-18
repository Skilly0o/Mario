import time

import pygame

from script.boss import Boss
from script.end_1level import End_1Level
from script.enemy import Enemy
from script.ground import Ground
from script.player import Player
from script.running_enemy import Enemy_run
from script.setting import *
from script.tile import Tile

pause_button = pygame.Rect(WIDTH - 150, 0, 150, 50)
continue_button = pygame.Rect((WIDTH - 200) // 2, (HEIGHT - 50) // 2, 200, 50)
quit_button = pygame.Rect((WIDTH - 200) // 2, ((HEIGHT - 50) // 2) + 100, 200, 50)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 20

    def update(self, speed):
        if speed > 0:
            self.rect.x += self.speedy
        elif speed < 0:
            self.rect.x -= self.speedy


class Level_boss:
    def __init__(self, level_data, surface):
        # настройки уровня
        self.display_surface = surface
        self.setup_level(level_data)

        self.last_jump_time = time.time()
        self.last_shot_time = time.time()
        self.shoot_interval = 2

        self.world_shift = 0
        self.end_level = False

        font = pygame.font.Font(None, 36)

    def setup_level(self, layout):
        # отрисовка лвла
        self.tiles = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.boss = pygame.sprite.GroupSingle()
        self.restart = False
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * title_size
                y = row_index * title_size
                if col == 'X':
                    tile = Tile((x, y), title_size)
                    self.tiles.add(tile)

                if col == 'G':
                    tile = Ground((x, y), title_size)
                    self.tiles.add(tile)

                if col == 'W':
                    tile = End_1Level((x, y), title_size)
                    self.tiles.add(tile)

                if col == 'P':
                    self.tile = Player((x, y))
                    self.player.add(self.tile)

                if col == 'B':
                    self.boses = Boss((x, y))
                    self.boss.add(self.boses)

                if col == 'E':
                    tile = Enemy((x, y), title_size)
                    self.tiles.add(tile)

                if col == 'R':
                    tile = Enemy_run((x, y), title_size)
                    self.tiles.add(tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < WIDTH / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > WIDTH - (WIDTH / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def shoot(self):
        boss = self.boss.sprite
        current_time = time.time()
        if current_time - self.last_shot_time >= self.shoot_interval:
            # Создать пулю (ваша реализация класса Bullet)
            bullet = Bullet(boss.rect.x, boss.rect.top)
            self.bullets.add(bullet)
            self.last_shot_time = current_time

    def horizontal_movment_collision(self, is_pause):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if str(sprite) == "<Enemy_run Sprite(in 1 groups)>":
                if sprite.life:
                    for i in self.tiles.sprites():
                        if str(i) != "<Enemy_run Sprite(in 1 groups)>":
                            if sprite.rect.colliderect(i.rect):
                                sprite.update(0, cos=True)
                                break
                    else:
                        sprite.update(0, is_pause=is_pause)
                else:
                    if sprite.y <= 4:
                        sprite.update(0, up=True)
                    elif 4 < sprite.y <= 20:
                        sprite.update(0, down=True)
                    elif 20 < sprite.y < 22:
                        sprite.update(0, down_down=True)

            if sprite.rect.colliderect(player.rect):
                # Проверяем просто это стена или враг
                if str(sprite) == "<Enemy Sprite(in 1 groups)>":
                    self.tile.life = False
                    self.restart = True

                if str(sprite) == "<Enemy_run Sprite(in 1 groups)>":
                    if sprite.life:
                        sprite.update(0)
                        self.tile.life = False
                        self.restart = True

                # проверка на конец лвла
                if str(sprite) == "<End_1Level Sprite(in 1 groups)>":
                    self.end_level = True

                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def enemy_collision_reverse(self):
        boss = self.boss.sprite
        if pygame.sprite.spritecollide(boss, self.tiles, False):
            boss.reverse()

    def check_enemy_collisions(self):
        player = self.player.sprite
        for sprite in self.boss.sprites():
            if sprite.rect.colliderect(player.rect):

                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    self.restart = True
                elif player.direction.x > 0:
                    self.restart = True
                    player.rect.right = sprite.rect.left

                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    self.boses.damage()
                    player.direction.y = -20

    def check_bull_collisions(self):
        player = self.player.sprite
        for sprite in self.bullets.sprites():
            if sprite.rect.colliderect(player.rect):

                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    sprite.kill()
                    self.restart = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    sprite.kill()
                    self.restart = True

                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    sprite.kill()
                    self.restart = True

                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    sprite.kill()
                    self.restart = True

    def bull_collision_title(self):
        for bullet in self.bullets.sprites():
            if pygame.sprite.spritecollide(bullet, self.tiles, False):
                bullet.kill()

    def vertical_movment_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        try:
            boss = self.boss.sprite
            boss.apply_gravity()
        except:
            print('Босс побежден')
            self.end_level = False
            boss = player

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # Проверяем просто это стена или враг
                if str(sprite) == "<Enemy Sprite(in 1 groups)>":
                    self.tile.life = False
                    self.restart = True
                if str(sprite) == "<Enemy_run Sprite(in 1 groups)>":
                    sprite.update(0, death=True)
                # проверка на конец лвла
                if str(sprite) == "<End_1Level Sprite(in 1 groups)>":
                    self.end_level = True
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.on_ground = True
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
            # физика босса
            if sprite.rect.colliderect(boss.rect):
                if boss.direction.y > 0:
                    boss.rect.bottom = sprite.rect.top
                    boss.direction.y = 0
                elif boss.direction.y < 0:
                    boss.rect.top = sprite.rect.bottom
                    boss.direction.y = 0

    def run(self, is_pause3):
        # Отрисовка спрайтов блоков
        self.tiles.update(self.world_shift, is_pause=is_pause3)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        self.shoot()

        # Босс и пульки его
        self.boss.update(self.world_shift, is_pause3)
        self.bull_collision_title()
        self.check_bull_collisions()
        self.bullets.update(self.boses.speed)
        self.bullets.draw(self.display_surface)

        self.enemy_collision_reverse()
        self.check_enemy_collisions()
        self.boss.draw(self.display_surface)

        # Отрисовка спрайтов игрока
        self.player.update(is_pause3)
        self.horizontal_movment_collision(is_pause3)
        self.vertical_movment_collision()
        self.player.draw(self.display_surface)
        font = pygame.font.Font(None, 36)
        pause_text = font.render("Pause", True, "black")
        pygame.draw.rect(self.display_surface, "yellow", pause_button)
        self.display_surface.blit(font.render("Pause", True, "black"),
                                  (pause_button.x + 40, pause_button.y + 15))
        if is_pause3:
            pygame.draw.rect(self.display_surface, "Green", continue_button)
            self.display_surface.blit(font.render("Continue", True, "black"),
                                      (continue_button.x + 40, continue_button.y + 15))
            pygame.draw.rect(self.display_surface, "red", quit_button)
            self.display_surface.blit(font.render("Quit", True, "black"),
                                      (quit_button.x + 70, quit_button.y + 15))
