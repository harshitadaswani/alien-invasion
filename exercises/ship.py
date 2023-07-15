import pygame


class Ship:
    """A class to manage ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # get_rect is a pygame method which considers elements as rectangles

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        """update the ship's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = int(self.x)

    def blitme(self):
        """Draw the ship at current location"""
        self.screen.blit(self.image, self.rect)
