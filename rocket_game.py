import sys
import pygame
from time import sleep
from rocket import Rocket
from rocket_settings import Settings
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class Rocket_game:
    """class that defines the behavior of rocket and its attributes"""

    def __init__(self):
        """initializes the behavior of attributes"""
        pygame.init()
        self.settings = Settings()
        self.stats = GameStats(self)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Rocket game window")
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "play")
        self.scoreboard = Scoreboard(self)

    def run_game(self):
        """starts the main loop of the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.rocket.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Responds to key and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """helper function which checks for keydown event"""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rocket.moving_down = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.rocket.moving_left = True
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.rocket.moving_right = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """helper function which checks for keyup event"""
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.rocket.moving_down = False
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.rocket.moving_right = False

    def _check_play_button(self, mouse_pos):
        """start a new game when player clicks play"""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.stats.reset_stats()
            self.settings.initialize_dynamic_settings()
            self.stats.game_active = True
            self.scoreboard.prep_score()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.rocket.center_rocket()
            pygame.mouse.set_visible(False)

    def _create_fleet(self):
        """create the fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (alien_width)
        # // is floor division
        number_aliens_x = available_space_x // (2*alien_width)
        rocket_height = self.rocket.rect.height
        available_space_y = (self.settings.screen_height) - \
            (3*alien_height) - rocket_height
        number_rows = available_space_y//(2*alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop the entire fleet and change fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        """create a new bullet and add it to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_alien(self, alien_number, row_number):
        """create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _rocket_hit(self):
        """Respond to the rocket being hit by the alien"""
        if self.stats.rockets_left > 0:
            self.stats.rockets_left -= 1
            # self.stats.rockets_left -= 1
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.rocket.center_rocket()
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """check if fleet is at the edge and then update the positions of all the aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            # print("Rocket Hit!")
            self._rocket_hit()
        self._check_aliens_bottom()

    def _update_bullets(self):
        """update position of bullets and get rid of old bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """respond to bullet alien-collisions"""
        # remove collided bullets and aliens
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points*len(aliens)
            self.scoreboard.prep_score()
        if not self.aliens:
            # destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _check_aliens_bottom(self):
        """check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._rocket_hit()
                break

    def _update_screen(self):
        """update images on the screem and flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.scoreboard.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()


if __name__ == "__main__":
    game = Rocket_game()
    game.run_game()
