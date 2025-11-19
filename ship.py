'''Draws and updates player character; handles bool for firing bullets
'''

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal



class Ship:

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image1 = self.load(self.light_mage1)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.arsenal = arsenal

    def update(self) -> None:
        # updating position of ship
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        # uses ship_speed in settings to determine how quickly the player can move with arrow keys
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self) -> None:
        # draws player sprite visually on screen
        self.arsenal.draw()
        iterate = 0
        animate = True
        while animate:
            if iterate >= len(self.light_mage):
                iterate = 0
            self.screem.blit(self.image1[iterate], self.rect)

    def fire(self) -> bool:
        # returns bool based on if player is able to fire a bullet
        return self.arsenal.fire_bullet()