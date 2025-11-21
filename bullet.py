'''Loads, draws, and moves bullet
'''

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion'):
        """initialize bullet settings and loads sprite"""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
                (self.settings.bullet_w, self.settings.bullet_h)
                )
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """moves bullet based on bullet_speed in settings"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """draws bullet visually on screen"""
        self.screen.blit(self.image, self.rect)