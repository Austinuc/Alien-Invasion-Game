import pygame
from settings.settings import Settings

class Ship():
    def __init__(self, screen, ai_settings:Settings):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.SHIP_SIZE = (ai_settings.screen_width // 5, ai_settings.screen_height // 8)

        # Game settings
        self.settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('./images/ship.bmp')
        self.image = pygame.transform.scale(self.image, self.SHIP_SIZE)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Store a decimal value for the ship's center.
        self.center = float(self.screen_rect.centerx)

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and ((self.settings.screen_width - self.center - self.SHIP_SIZE[0]/2) > 0):
                self.center += self.settings.ship_speed_factor
        elif self.moving_left and (self.center - self.SHIP_SIZE[0]/2) > 0:
                self.center -= self.settings.ship_speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.center