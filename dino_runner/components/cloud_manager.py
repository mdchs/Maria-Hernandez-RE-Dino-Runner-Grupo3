from dino_runner.utils.constants import CLOUD
from dino_runner.components.clouds import Clouds

class CloudManager:
    def __init__(self):
        self.clouds = []

    def update(self, game):
        if len(self.clouds) < 1:
            self.clouds.append(Clouds(CLOUD))

        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)

    def draw(self, screen, night):
        for cloud in self.clouds:
            cloud.draw(screen, night)
        