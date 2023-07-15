import pygame


class Rocket:
    """A class to manage rocket"""

    def __init__(self, game):
        """initialize the rocket attributes"""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """update the ship's posiion based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        elif self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def blitme(self):
        """draw the rocket at current location"""
        self.screen.blit(self.image, self.rect)

    def center_rocket(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
