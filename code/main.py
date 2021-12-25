'''
Followed "Creating a platformer in Pygame with a camera, collisions, animation states and particle effects"
    (https://www.youtube.com/watch?v=YWN8GcmJ-jA) by Clear Code
Image Assets from "analogStudios_" on itch.io for the camelot_ pack (https://analogstudios.itch.io/camelot)
    and from "Pixel Frog" on itch.io for the Kings and Pigs tileset (https://pixelfrog-assets.itch.io/kings-and-pigs)
'''

import pygame, sys
from settings import *
from level import Level

# Pygame setup
pygame.init( )
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
