'''Handles bullet logic and ammo
'''

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        """initialize arsenal game settings and sprite group"""
        self.game = game
        self.settings = game.settings
        
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """updates arsenal by using methods defined under class Arsenal"""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """removes a bullet from arsenal list if it is fully off screen"""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """uses draw_bullet() method to draw bullet on screen"""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """bool for if there are few enough bullets on screen to fire another one"""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    
