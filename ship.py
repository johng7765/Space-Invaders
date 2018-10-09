# ship.py
# Created by: John Gawlik
# Campus ID: 889752424
# Due: September 21st, 2018
########################################################################################################################
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.images = []
        self.images.append(pygame.image.load('images/ship.gif'))
        self.images.append(pygame.image.load('images/ship_blowup/ship_blowup_1.gif'))
        self.images.append(pygame.image.load('images/ship_blowup/ship_blowup_2.gif'))
        self.images.append(pygame.image.load('images/ship_blowup/ship_blowup_3.gif'))
        self.images.append(pygame.image.load('images/ship_blowup/ship_blowup_4.gif'))
        self.images.append(pygame.image.load('images/ship_blowup/ship_blowup_5.gif'))
        self.images.append(pygame.image.load('images/ship_blowup/ship_blowup_6.gif'))
        self.images.append(pygame.image.load('images/ship_blowup/ship_blowup_7.gif'))
        self.images.append(pygame.image.load('images/ship_blowup/ship_blowup_8.gif'))
        self.images.append(pygame.image.load('images/ship_blowup/ship_blowup_9.gif'))
        self.images.append(pygame.image.load('images/ship_blowup/ship_blowup_10.gif'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        self.hit = False
        self.last = pygame.time.get_ticks()
        self.wait = 6

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at tis current location."""
        image = self.images[0]
        if self.hit:
            now = pygame.time.get_ticks()
            if (now - self.last) >= self.wait:
                image = self.images[self.index]
                self.index += 1
                self.last = now

                if self.index >= len(self.images):
                    self.index = 0
                    self.hit = False
        self.screen.blit(image, self.rect)


