import pygame
import pytmx
import os

os.chdir('D:\\AllPythonProjeckt\\Mario')
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('загрузка карты Tiled в Pygame')

class Levels_1:
    def __init__(self, free_tile, finish_tile):
        self.map = pytmx.load_pygame('data/maps/mariomap.tmx')
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.free_tile = free_tile
        self.finish_tile = finish_tile

    def render(self, screen):
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.map.get_tile_image_by_gid(gid)
                    screen.blit(tile, (x * self.tile_size, y * self.tile_size))

    def get_tile_id(self, position):
        return self.map.get_tile_gid(*position, 0)

# levels = Levels_1(0, 0)
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((255, 255, 255))
#     levels.render(screen)
#     pygame.display.flip()
#
# pygame.quit()