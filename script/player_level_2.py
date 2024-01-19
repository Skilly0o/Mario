import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.images = [pygame.image.load('script/data/textures/player.png').convert_alpha(),
                       pygame.image.load('script/data/textures/player_2.png').convert_alpha(),
                       pygame.image.load('script/data/textures/player_3.png').convert_alpha()]
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        self.life = True

    def get_input(self, is_pause2):
        if not is_pause2:
            if self.life:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_RIGHT]:
                    self.direction.x = 1
                elif keys[pygame.K_LEFT]:
                    self.direction.x = -1
                else:
                    self.direction.x = 0

                if keys[pygame.K_UP]:
                    self.jump()

    def x(self):
        return self.life

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self, is_pause2):
        self.get_input(is_pause2)
        if self.direction.x != 0:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
            self.image = self.images[self.current_image]
