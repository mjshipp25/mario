'''
Followed "Creating a platformer in Pygame with a camera, collisions, animation states and particle effects"
    (https://www.youtube.com/watch?v=YWN8GcmJ-jA) by Clear Code
    and "Creating a Mario style level in Python / Pygame with a visual level editor [Tiled]"
    (https://www.youtube.com/watch?v=wJMDh9QGRgs&t=26s) by Clear Code
    
Image Assets from "analogStudios_" on itch.io for the camelot_ pack (https://analogstudios.itch.io/camelot)
    and from "Pixel Frog" on itch.io for the Kings and Pigs tileset (https://pixelfrog-assets.itch.io/kings-and-pigs)
'''

import sys

import pygame

from game_data import level_0, level_1
from level import Level
from levelselect import LevelSelect
from settings import *

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level_select = LevelSelect()
level = Level(level_select, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('gray')
    level.run()

    pygame.display.update()
    clock.tick(60)
