import pygame

class Scoreboard:
    """A class to report scoring information"""

    def __init__(self, game):
        """initialize scorekeeping attributes"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont("sans-serif", 48)
        self.prep_score()

    def prep_score(self):
        """turn score into rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = 20

    def show_score(self):
        """draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)