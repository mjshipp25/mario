import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size)) # x, y
        self.rect = self.image.get_rect(topleft = (x, y))
        self.image.fill('gray')

    def update(self, x_shift):
        self.rect.x += x_shift