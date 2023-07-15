import pygame

class Bird_character:
    """A class to manage bird character"""

    def __init__(self, c_game):
        """initialize character and its current position"""
        self.screen = c_game.screen 
        self.screen_rect = c_game.screen.get_rect()
        self.image = pygame.image.load("images/bird_small.bmp")
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the bird at current location"""
        self.screen.blit(self.image, self.rect)