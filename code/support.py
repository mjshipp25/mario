import pygame
from csv import reader 
from os import walk
from settings import tile_size

def import_folder(path, bool, scale):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            # image_surf.set_colorkey('black') 
            if bool:     
                x, y = image_surf.get_width() * scale, image_surf.get_height() * scale
                new_image_surf = pygame.Surface((x, y)).convert_alpha()
                pygame.transform.scale(image_surf, (x, y), new_image_surf)
                image_surf = new_image_surf
            surface_list.append(image_surf)

    return surface_list

def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            terrain_map.append(list(row))
    return terrain_map

def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_width() / tile_size)
    tile_num_y = int(surface.get_height() / tile_size)

    for row in range(tile_num_x):
        for col in range(tile_num_y):
            x = col * tile_size
            y = row * tile_size
            new_surface = pygame.Surface((tile_size, tile_size))
            new_surface.blit(surface, )

