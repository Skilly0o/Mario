import pygame

from script.end_1level import End_1Level
from script.enemy import Bad_trub, Bad_pipe
from script.ground import Pipe
from script.player_level_2 import Player
from script.running_enemy import Enemy_run
from script.setting import *
from script.tile import Up_pipe

pause_button = pygame.Rect(WIDTH - 150, 0, 150, 50)
continue_button = pygame.Rect((WIDTH - 200) // 2, (HEIGHT - 50) // 2, 200, 50)
quit_button = pygame.Rect((WIDTH - 200) // 2, ((HEIGHT - 50) // 2) + 100, 200, 50)


class Level_2:
    def __init__(self, level_data, surface):
        # настройки уровня
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0
        self.end_level = False

        self.font = pygame.font.Font(None, 36)

    def setup_level(self, layout):
        # отрисовка лвла
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.restart = False
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                x = col_index * title_size
                y = row_index * title_size
                if col == 'X':  # cтоячие блоки
                    tile = Up_pipe((x, y), title_size)
                    self.tiles.add(tile)

                if col == 'G':  # подземные блоки
                    tile = Pipe((x, y), title_size)
                    self.tiles.add(tile)

                if col == 'K':  # УБИЙЦЫ ТРУБЫ блоки
                    tile = Bad_pipe((x, y), title_size)
                    self.tiles.add(tile)

                if col == 'W':  # финиш
                    tile = End_1Level((x, y), title_size)
                    self.tiles.add(tile)

                if col == 'P':  # Игрок
                    self.tile = Player((x, y))
                    self.player.add(self.tile)

                if col == 'E':  # стоячий враг
                    tile = Bad_trub((x, y), title_size)
                    self.tiles.add(tile)

                if col == 'R':  # ходячий враг
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
                if sprite.life:
                    for i in self.tiles.sprites():
                        if str(i) != "<Enemy_run Sprite(in 1 groups)>":
                            if sprite.rect.colliderect(i.rect):
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

            if sprite.rect.colliderect(player.rect):
                # Проверяем просто это стена или враг
                if str(sprite) == "<Bad_trub Sprite(in 1 groups)>" or str(sprite) == "<Bad_pipe Sprite(in 1 groups)>":
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

    def vertical_movment_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):

                # Проверяем просто это стена или враг
                if str(sprite) == "<Bad_trub Sprite(in 1 groups)>" or str(sprite) == "<Bad_pipe Sprite(in 1 groups)>":
                    self.tile.life = False
                    self.restart = True

                if str(sprite) == "<Enemy_run Sprite(in 1 groups)>":
                    sprite.update(0, death=True)

                # проверка на конец лвла
                if str(sprite) == "<End_1Level Sprite(in 1 groups)>":
                    self.end_level = True

                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self, is_pause2):
        # Отрисовка спрайтов блоков
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # Отрисовка спрайтов игрока
        self.player.update(is_pause2)
        self.horizontal_movment_collision()
        self.vertical_movment_collision()
        self.player.draw(self.display_surface)

        font = pygame.font.Font(None, 36)
        pause_text = font.render("Pause", True, "black")
        pygame.draw.rect(self.display_surface, "yellow", pause_button)
        self.display_surface.blit(font.render("Pause", True, "black"),
                                  (pause_button.x + 40, pause_button.y + 15))
        if is_pause2:
            pygame.draw.rect(self.display_surface, "Green", continue_button)
            self.display_surface.blit(self.font.render("Continue", True, "black"),
                                      (continue_button.x + 40, continue_button.y + 15))
            pygame.draw.rect(self.display_surface, "red", quit_button)
            self.display_surface.blit(self.font.render("Quit", True, "black"),
                                      (quit_button.x + 70, quit_button.y + 15))
