from dino_runner.utils.constants import HAMMER, SCREEN_WIDTH
from pygame.sprite import Sprite

class Hammer(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.speedy
        if self.rect.left < SCREEN_WIDTH:
            self.kill()



