import sys
import pygame
from settings import Settings
from character import Bird_character


class Game_character:
    """a class to represent game behavior and assets"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.bg_color = (0, 0, 0)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Game Character Window")
        self.bird = Bird_character(self)

    def run_game(self):
        """starts the main loop of the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.bird.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    c_game = Game_character()
    c_game.run_game()
