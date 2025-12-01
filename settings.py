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
        '''Increased difficulty scale from 1.1 to 1.3, since fleet shape makes game easier'''
        self.difficulty_scale = 1.3
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'
        
        
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'lightMage.png'
        self.ship_w = 40
        self.ship_h = 60

        '''Implemented new music for the background, although only one song is utilized.'''
        self.menu_theme = Path.cwd() / 'Assets' / 'music' / 'PythonGameMenu.mp3'
        self.main_theme = Path.cwd() / 'Assets' / 'music' / 'PythonGameMainTheme.mp3'
        self.game_over_theme = Path.cwd() / 'Assets' / 'music' / 'PythonGameGameOver.mp3'

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'pixelFireball.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'fireballSound.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'fire_impact.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'skeleton_enemy.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1

        '''Button is now much wider to fit new text'''
        self.button_w = 600
        self.button_h = 100
        '''Button color is now a dusky brown to fit aesthetic better'''
        self.button_color = (135,117,61)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        '''Font is now a more medieval, fantasy style'''
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Cinzel-Regular.ttf'

    def initialize_dynamic_settings(self):
        '''settings that can change based on difficulty'''
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed = 7
        self.bullet_amount = 5
        
        self.fleet_speed = 5
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self):
        '''changes speed settings of player, bullet, enemy using difficulty scale'''
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale
