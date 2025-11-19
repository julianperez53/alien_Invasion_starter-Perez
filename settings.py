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
        # Changed bg_file to new cryptBG art
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'cryptBG.png'

        self.light_mage = []
        self.light_mage1 = Path.cwd() / 'Assets' / 'images' / 'Light Mage' / 'lightMageF1'

        value = 1
        while value < 9:
            self.light_mage.append(Path.cwd() / 'Assets' / 'images' / 'Light Mage' / ('lightMageF' + str(value)))
            value += 1
        
        # Changed ship_file to new lightMage art
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'lightMage.png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        # Changed bullet_file to pixelFireball and laser_sound to fireballSound
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'pixelFireball.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'fireballSound.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5