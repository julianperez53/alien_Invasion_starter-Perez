"""Game where player fires at incoming enemies.
Alien Invasion
Julian Perez
11/14/2025
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal

'''Lab 12, Option 2: Custom Assets.
I drew original pixel art for a new player sprite, a unique attack, and a new background.
To completely change the aesthetic of the game, the player is now a mage that fires fireballs.
The background is the entrance to a crypt.
The new firing sound effect is "Fireball Whoosh 2" by floraphonic from pixabay.com,
which provides a free library of sound effects with no license or credit requirements.
'''

class AlienInvasion:
    """Initialize and run game, check key presses"""
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,(self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))

    def run_game(self) -> None:
        """Game loop"""
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self) -> None:
        """Draws background and updates frames of game"""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self) -> None:
        """Checks events for pressing/releasing keys or quitting"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

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
            pygame.quit()
            sys.exit()






if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
