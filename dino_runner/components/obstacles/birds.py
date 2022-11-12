import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, BIRD
from dino_runner.components.invertcolor import InvertirColor

class Birds(Sprite):
    def __init__(self):
        self.image = BIRD[0]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 245
        self.index = 0
        self.invertir_color = InvertirColor()

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed / 2
        if self.rect.x < -self.rect.width and obstacles:
            obstacles.pop()

        if self.index >= 10:
            self.index = 0
    
    def draw(self, screen, night):
        if night:
            self.invertir_color.invert(self.image, (83,83,83), (255, 255, 254))
        else:
            self.invertir_color.invert(self.image, (255, 255, 254), (83,83,83))
        self.image = BIRD[0] if self.index < 5 else BIRD[1]
        self.rect.x = self.rect.x
        self.index += 1
        screen.blit(self.image, (self.rect.x, self.rect.y))
