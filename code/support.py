import pygame
from os import walk

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

