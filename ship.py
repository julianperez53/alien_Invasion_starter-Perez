'''Draws and updates player character; handles bool for firing bullets
'''

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal



class Ship:

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        """Initializes ship settings and loads sprite"""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        """centers ship at middle bottom screen"""
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self) -> None:
        """updates position of ship"""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """uses ship_speed in settings to determine how quickly the player can move with arrow keys"""
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self) -> None:
        """draws player sprite visually on screen"""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """returns bool based on if player is able to fire a bullet"""
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        """checks ship collision with specific sprite group"""
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False