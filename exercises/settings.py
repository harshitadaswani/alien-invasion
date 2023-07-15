class Settings:
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """Initialize game settings"""
        # screen settings
        self.screen_width = 1550
        self.screen_height = 800
        # sets bg_color attribute to somne value
        self.bg_color = (230, 230, 230)
        # (230 230 230) has equal proportion of rgb and produces light gray color
        self.ship_speed = 1.5
