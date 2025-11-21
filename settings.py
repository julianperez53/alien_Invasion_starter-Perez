'''Settings for integer values and assets
'''

from pathlib import Path
import pygame
from pygame.locals import *

class Settings:
    def __init__(self) -> None:
        self.name: str = "Alien Invasion"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'cryptBG.png'
        
        
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'lightMage.png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5


        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'pixelFireball.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'fireballSound.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.fleet_speed = 5
        self.alien_w = 40
        self.alien_h = 40