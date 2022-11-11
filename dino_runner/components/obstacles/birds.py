import random
from dino_runner.utils.constants import SCREEN_WIDTH, BIRD

class Birds:
    def __init__(self):
        self.image = BIRD[0]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 245
        self.index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed / 2
        if self.rect.x < -self.rect.width and obstacles:
            obstacles.pop()

        if self.index >= 10:
            self.index = 0
    
    def draw(self, screen):
        self.image = BIRD[0] if self.index < 5 else BIRD[1]
        self.rect.x = self.rect.x
        self.index += 1
        screen.blit(self.image, (self.rect.x, self.rect.y))
