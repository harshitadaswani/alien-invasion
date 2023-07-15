import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """class to initialize bullets"""

    def __init__(self, game):
        """Create a bullet object at ships current position"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.rocket.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up in the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
