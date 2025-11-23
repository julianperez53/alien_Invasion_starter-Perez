import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion



class AlienFleet:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """fleet settings, size, offset, shape"""
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        self._create_pyramid_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """standard rectangle shape for fleet"""
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def _create_pyramid_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """unique half pyramid shape for fleet"""
        for row in range(1, fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col > (row + 1):
                    continue
                if col % 4 == 0 or row % 4 == 0:
                    continue
                self._create_alien(current_x, current_y)


    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """offsets for fleet creation based on screen size"""
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w-fleet_horizontal_space)//2)
        y_offset = int((half_screen-fleet_vertical_space)//2)
        return x_offset,y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """calculates amount of aliens able to be created"""
        fleet_w = (screen_w // alien_w)
        fleet_h = ((screen_h / 2) // alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2


        return int(fleet_w), int(fleet_h)
        
    def _create_alien(self, current_x: int, current_y: int):
        """utilizes imported Alien class to add aliens to fleet"""
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """checks if any alien has hit an edge; drops and switches entire fleet direction"""
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """drops all aliens in fleet down"""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        """moves fleet and checks edges"""
        self._check_fleet_edges()
        self.fleet.update()
        
    def draw(self):
        """draws aliens utilizing Alien class"""
        alien: 'Alien'
        for alien in self.fleet:
                alien.draw_alien()

    def check_collisions(self, other_group):
        """checks collisions of aliens in fleet with another sprite group"""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_bottom(self):
        """checks if any alien has hit bottom screen"""
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self):
        """bool True if no aliens left"""
        return not self.fleet