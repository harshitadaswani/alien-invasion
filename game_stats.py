class GameStats:
    """track statistics for the alien game"""

    def __init__(self, game):
        """Initialize statistics"""
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.rockets_left = self.settings.rocket_limit
        self.score = 0 
