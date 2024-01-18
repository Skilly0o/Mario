import pygame

from script.end_1level import End_1Level
from script.enemy import Enemy
from script.ground import Ground
from script.player import Player
from script.enemy import Enemy
from script.block import Block
from script.running_enemy import Enemy_run
from script.setting import *
from script.tile import Tile

pause_button = pygame.Rect(WIDTH - 150, 0, 150, 50)
continue_button = pygame.Rect((WIDTH - 200) // 2, (HEIGHT - 50) // 2, 200, 50)
quit_button = pygame.Rect((WIDTH - 200) // 2, ((HEIGHT - 50) // 2) + 100, 200, 50)


class Level:
    def __init__(self, level_data, surface):
        # настройки уровня
        self.running = True
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0
        self.end_level = False

        font = pygame.font.Font(None, 36)

    def setup_level(self, layout):
        # отрисовка лвла
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.restart = False
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * title_size
                y = row_index * title_size
                if col == 'P':
                    self.tile = Player((x, y))
                    self.player.add(self.tile)

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

                if col == 'E':
                    tile = Enemy((x, y), title_size)
                    self.tiles.add(tile)

                if col == 'B':
                    tile = Block((x, y), title_size)
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
            down = True
            if str(sprite) == "<Enemy_run Sprite(in 1 groups)>" \
                    or str(sprite) == "<Block Sprite(in 1 groups)>":
                if sprite.life:
                    for i in self.tiles.sprites():
                        if i.rect.center != sprite.rect.center:
                            if i.rect.top == sprite.rect.bottom and (
                                    -64 < i.rect.center[0] - sprite.rect.center[0] < 64) and \
                                    str(sprite) == "<Block Sprite(in 1 groups)>":
                                down = False
                            if (i.rect.center[0] - sprite.rect.center[0] == 64 or i.rect.center[0] - sprite.rect.center[
                                0] == -64) and \
                                    str(sprite) == "<Block Sprite(in 1 groups)>" and i.rect.center[1] == \
                                    sprite.rect.center[1]:
                                sprite.update(0, cos=True)
                            if sprite.rect.colliderect(i.rect) and str(sprite) != "<Block Sprite(in 1 groups)>":
                                sprite.update(0, cos=True)
                                break
                    else:
                        sprite.update(0)
                else:
                    if sprite.y <= 4:
                        sprite.update(0, up=True)
                    elif 4 < sprite.y <= 20:
                        sprite.update(0, down=True)
                    elif 20 < sprite.y < 22:
                        sprite.update(0, down_down=True)
            if down and str(sprite) == "<Block Sprite(in 1 groups)>":
                sprite.update(16, down=True)
                sprite.update(player.direction.x * 8)
                if sprite.rect.center[1] > 1200:
                    sprite.update(5000, down=True)
                    sprite.wall = False

            if sprite.rect.colliderect(player.rect):
                # Проверяем просто это стена или враг
                if str(sprite) == "<Enemy Sprite(in 1 groups)>":
                    self.tile.life = False
                    self.restart = True

                if str(sprite) == "<Enemy_run Sprite(in 1 groups)>":
                    if sprite.life:
                        self.tile.life = False
                        self.restart = True

                # проверка на конец лвла
                if str(sprite) == "<End_1Level Sprite(in 1 groups)>":
                    self.end_level = True

                if str(sprite) == "<Block Sprite(in 1 groups)>":
                    if sprite.wall:
                        sprite.update(player.direction.x * 8)

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

    def run(self, is_pause1):
        # Отрисовка спрайтов блоков
        self.tiles.update(self.world_shift, is_pause1)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # Отрисовка спрайтов игрока
        self.player.update(is_pause1)
        self.horizontal_movment_collision()
        self.vertical_movment_collision()
        self.player.draw(self.display_surface)
        font = pygame.font.Font(None, 36)
        pause_text = font.render("Pause", True, "black")
        pygame.draw.rect(self.display_surface, "yellow", pause_button)
        self.display_surface.blit(font.render("Pause", True, "black"),
                                  (pause_button.x + 40, pause_button.y + 15))
        if is_pause1:
            pygame.draw.rect(self.display_surface, "Green", continue_button)
            self.display_surface.blit(font.render("Continue", True, "black"),
                                      (continue_button.x + 40, continue_button.y + 15))
            pygame.draw.rect(self.display_surface, "red", quit_button)
            self.display_surface.blit(font.render("Quit", True, "black"),
                                      (quit_button.x + 70, quit_button.y + 15))
