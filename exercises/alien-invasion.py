import sys  # import system modules helpful when exit operation is performed by the user

import pygame  # import pygame modules to make a game where w can just focus on the logic

from settings import Settings  # importing settings from settings module

from ship import Ship  # importing ship from ship module


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and its resources"""
        self.settings = Settings()
        pygame.init()  # initializes the background settings for pygame to work properly
        # creates a display window where game's graphical elements are created
        # self.screen = pygame.display.set_mode(
        #     (self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode(
            (0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # (1568,800) is a tuple that defines the dimensions of the window
        # pygame.display.set_mode is an object called a surface which is assigned to self.screen
        # surface is a part of a screen where a game element can be displayed. Each element has it's own suface
        # surface of display.set_mode represents the entire game window
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):  # game is controlled by this method
        """Starts the main loop of the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():  # event is an action that user performs while interacting
            # pygame.event.get() accesses the events that pygame detects
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Update images on the screen and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        # fills the screen with specified background color
        self.ship.blitme()
        pygame.display.flip()  # pygame makes the most recently drawn screen visible
        # here it draws an empty screen on each pass through the loop
        # .flip continously updates the display to show new elements and hide old ones


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
