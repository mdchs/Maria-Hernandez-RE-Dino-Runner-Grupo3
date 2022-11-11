from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.components.invertcolor import InvertirColor

class Obstacle(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.invertir_color = InvertirColor()

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed / 2
        if self.rect.x < -self.rect.width and obstacles:
            obstacles.pop()

    def draw(self, screen, night):
        imagen = self.image[self.type]
        if night:
            self.invertir_color.invert(imagen, (83,83,83), (255, 255, 254))
        else:
            self.invertir_color.invert(imagen, (255, 255, 254), (83,83,83))
        screen.blit(imagen, self.rect)


