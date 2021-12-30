import pygame
from tiles import AnimatedTile
from random import randint
from support import scale

class Enemy(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, '../graphics/enemy/run')
        self.frames = scale(self.frames, 2.5)
        self.image = self.frames[self.frame_index]
        self.rect.y += size - self.image.get_height()
        self.speed = randint(3, 5)
        
    def move(self):
        self.rect.x += self.speed        

    def reverse_image(self):
        if self.speed < 0:
            self.image = pygame.transform.flip (self.image, True, False) # x, y
        
    def reverse(self):
        self.speed *= -1

    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
        self.reverse_image()
