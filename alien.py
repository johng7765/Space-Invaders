# alien.py
# Created by: John Gawlik
# Campus ID: 889752424
# Due: September 21st, 2018
########################################################################################################################
import pygame
import random
from pygame.sprite import Sprite


class AlienTop(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(AlienTop, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.images = []
        self.images.append(pygame.image.load('images/alien_top_1.gif'))
        self.images.append(pygame.image.load('images/alien_top_2.gif'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    """def blow_up(self):
        self.images.clear()
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_1.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_2.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_3.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_4.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_5.gif'))
        self.index = 0"""

    def check_edges(self):
        """Return True if alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        if pygame.time.get_ticks() % 100 == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

        """Move the alien right."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


class AlienMiddle(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(AlienMiddle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.images = []
        self.images.append(pygame.image.load('images/alien_middle_1.gif'))
        self.images.append(pygame.image.load('images/alien_middle_2.gif'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    """def blow_up(self):
        self.images.clear()
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_1.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_2.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_3.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_4.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_5.gif'))
        self.index = 0"""

    def check_edges(self):
        """Return True if alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        if pygame.time.get_ticks() % 100 == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        """Move the alien right."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


class AlienBottom(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(AlienBottom, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.images = []
        self.images.append(pygame.image.load('images/alien_bottom_1.gif'))
        self.images.append(pygame.image.load('images/alien_bottom_2.gif'))
        self.index = 0
        self.image = self.images[self.index]
        self.blow_up = []
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    """def blow_up(self):
        self.images.clear()
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_1.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_2.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_3.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_4.gif'))
        self.images.append(pygame.image.load('images/alien_blowup/alien_blowup_5.gif'))
        self.index = 0"""

    def check_edges(self):
        """Return True if alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        if pygame.time.get_ticks() % 100 == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        """Move the alien right."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


class Ufo(Sprite):
    """A class to represent the UFO"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Ufo, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.images = []
        self.images.append(pygame.image.load('images/UFO/UFO.gif'))
        self.images.append(pygame.image.load('images/UFO/UFO_100.gif'))
        self.images.append(pygame.image.load('images/UFO/UFO_200.gif'))
        self.images.append(pygame.image.load('images/UFO/UFO_300.gif'))
        self.images.append(pygame.image.load('images/UFO/UFO_400.gif'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new UFO near the top left of the screen.
        self.rect.x = self.screen_rect.left
        self.rect.y = self.screen_rect.top + 100

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.left >= screen_rect.right:
            return True

    def center_ufo(self):
        """Center the ship on the screen."""
        self.x = self.screen_rect.left - 100

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def blow_up(self):
        if self.index >= 1:
            return False
        else:
            self.index = random.randint(1, 4)
            self.image = self.images[self.index]
            if self.index == 1:
                return self.ai_settings.ufo_points_100
            elif self.index == 2:
                return self.ai_settings.ufo_points_200
            elif self.index == 3:
                return self.ai_settings.ufo_points_300
            elif self.index == 4:
                return self.ai_settings.ufo_points_400

    def reset_image(self):
        self.index = 0
        self.image = self.images[self.index]

    def update(self):
        """Move the alien right."""
        self.x += self.ai_settings.ufo_speed_factor
        self.rect.x = self.x
