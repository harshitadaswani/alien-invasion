import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """class to represent a simngle alien"""

    def __init__(self, game):
        """initialize alien and set its starting position"""
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.settings = game.settings

    def update(self):
        """move alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
