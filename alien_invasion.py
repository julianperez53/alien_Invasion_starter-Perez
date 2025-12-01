"""Game where player fires at incoming enemies.
Alien Invasion
Julian Perez
12/01/2025
"""

import sys
import pygame
from pygame import mixer
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from time import sleep
from button import Button
from hud import HUD


'''Lab 14, Custom Assets.
I implemented a unique song in the background that I composed in MuseScore.
Pygame's music mixer was giving me a lot of trouble, so I was unable
to implement the different songs I had planned for different conditions
(such as main menu or game over).
Using Google Fonts, I adjusted the font to be more medieval fantasy themed.
I updated the play button to have "Enter the Crypt" as the text, 
with a larger play button to accomodate.
I adjusted the difficulty scale since the shape of the fleet makes the game easier.
I added docstrings to all new and updated code.
'''

class AlienInvasion:
    """Initialize and run game, music plays, check key presses"""
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,(self.settings.screen_w, self.settings.screen_h))

        self.game_stats = GameStats(self)
        self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        mixer.init()
        self.laser_sound = mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.9)

        self.impact_sound = mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        # self.menu_theme = pygame.mixer.music.load(self.settings.menu_theme)
        # self.menu_theme.set_volume(0.5)

        mixer.music.load(self.settings.main_theme)
        mixer.music.set_volume(0.3)
        mixer.music.play(-1)


        # self.game_over_theme = pygame.mixer.music.load(self.settings.game_over_theme)
        # self.game_over_theme.set_volume(0.5)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        '''Play button now says Enter the Crypt instead of Play
        to immerse player in magical setting'''
        self.play_button = Button(self, 'Enter the Crypt')
        self.game_active = False

    def run_game(self) -> None:
        """Game loop"""
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)




    def _check_collisions(self):
        """check collisions for ship with aliens and aliens with projectiles and bottom of screen
        updates score if alien is killed"""
        # check collisions for ship
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
            # subtract one life if possible

        # check collisions for aliens and bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()


        # check collisions of projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(300)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroyed_status():
            '''if player defeats fleet, level resets, difficulty increases,
            HUD and level stats are updated'''
            self._reset_level()
            self.settings.increase_difficulty()
            # update game stats level
            self.game_stats.update_level()
            # update HUD view
            self.HUD.update_level()

    def _check_game_status(self):
        """check lives left and reset level if none left"""
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    def _reset_level(self):
        """ship recenters and recreates alien fleet at top screen"""
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self):
        '''restarts games and resets stats'''
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        '''Level indicator previously did not reset to 1 upon game over and reset'''
        self.HUD.update_level()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)

    def _update_screen(self) -> None:
        """Draws background and updates frames of game
        if game is not active, mouse is visible"""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        self.alien_fleet.draw()
        self.HUD.draw()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
        pygame.display.flip()

    def _check_events(self) -> None:
        """Checks events for pressing/releasing keys or quitting
        checks clicking of play button to activate game"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.game_stats.save_scores()
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and self.game_active == True:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    # keyup events stop the ship from moving if direction keys no longer pressed
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # keydown events move the ship with direction keys and fire with space bar, playing a sound effect whenever firing is successful.
    # q to quit
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            self.game_stats.save_scores()
            pygame.quit()
            sys.exit()






if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
