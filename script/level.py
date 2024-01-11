import pygame
from script.tile import Tile
from script.ground import Ground
from script.setting import *
from script.player import Player
from script.enemy import Enemy
from script.running_enemy import Enemy_run


class Level:
    def __init__(self, level_data, surface):
        # настройки уровня
        self.display_suface = surface
        self.setup_level(level_data)

        self.world_shift = 0

    def setup_level(self, layout):
        # отрисовка лвла
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
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

                if col == 'P':
                    self.tile = Player((x, y))
                    self.player.add(self.tile)

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

    def horizontal_movment_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if str(sprite) == "<Enemy_run Sprite(in 1 groups)>":
                for i in self.tiles.sprites():
                    if str(i) != "<Enemy_run Sprite(in 1 groups)>":
                        if sprite.rect.colliderect(i.rect):
                            sprite.update(0, cos=True)
                            break
                else:
                    sprite.update(0)

            if sprite.rect.colliderect(player.rect):
                # Проверяем просто это стена или враг
                if str(sprite) == "<Enemy Sprite(in 1 groups)>":
                    sprite.update(0)
                    self.tile.life = False
                    self.restart = True
                if str(sprite) == "<Enemy_run Sprite(in 1 groups)>":
                    sprite.update(0)
                    self.tile.life = False
                    self.restart = True
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movment_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                # Проверяем просто это стена или враг
                if str(sprite) == "<Enemy Sprite(in 1 groups)>":
                    sprite.update(0)
                    self.tile.life = False
                    self.restart = True
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.on_ground = True
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        # Отрисовка спрайтов блоков
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_suface)
        self.scroll_x()

        # Отрисовка спрайтов игрока
        self.player.update()
        self.horizontal_movment_collision()
        self.vertical_movment_collision()
        self.player.draw(self.display_suface)
