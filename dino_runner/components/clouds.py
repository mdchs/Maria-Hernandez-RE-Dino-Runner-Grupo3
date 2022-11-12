from pygame.sprite import Sprite
import random
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.components.invertcolor import InvertirColor


class Clouds(Sprite):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, 350)
        self.invertir_color = InvertirColor()

    def update(self, game_speed, clouds):
        self.rect.x -= game_speed / 2
        if self.rect.x < -self.rect.width and clouds:
            clouds.pop()

    def draw(self, screen, night):
        if night:
            self.invertir_color.invert(self.image, (0, 0, 0), (255, 255, 254))
        else:
            self.invertir_color.invert(self.image, (255, 255, 254), (0, 0, 0))
        screen.blit(self.image, self.rect)
