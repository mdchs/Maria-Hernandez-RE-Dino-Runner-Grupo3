import pygame

class InvertirColor:
    def invert(self, image, color, newcolor):
        pixel_array = pygame.PixelArray(image) 
        pixel_array.replace(color, newcolor, 0)
        pixel_array.make_surface()