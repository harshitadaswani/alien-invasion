# 12-1. Blue Sky: Make a Pygame window with a blue background.

import sys
import pygame
from settings import Settings


class Blue_sky:
    """a class to manage assets and behaviors"""

    def __init__(self):
        """Initialize game and its resources"""
        pygame.init()
        self.settings = Settings()
        self.bg_color = (0, 0, 255)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("blue sky window")
        
    def run_game(self):
        """Starts the main loop of the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == "__main__":
    bs = Blue_sky()
    bs.run_game()