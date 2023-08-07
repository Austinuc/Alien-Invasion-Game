import pygame
from settings.settings import Settings

class Alien(pygame.sprite.Sprite):

    def __init__(self, screen, ai_settings:Settings, position=1):
        super().__init__()
        self.screen = screen
        self.settings = ai_settings
        self.ALIEN_SHIP_SIZE = (self.settings.screen_width // 5, self.settings.screen_height // 8)

        self.image = pygame.image.load('./images/alien.bmp')
        self.image = pygame.transform.scale(self.image, self.ALIEN_SHIP_SIZE)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.x = float(self.settings.ship_speed_factor)
        self.y = float(self.settings.ship_speed_factor)

        position = 1 if position < 1 else position
        self.rect.left = 30 + self.ALIEN_SHIP_SIZE[0] * (position - 1) + (30 if position > 1 else 0) * (position - 1)
        self.rect.top = 30

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        pass
        # self.x += 0.9 + 2.8
        # self.y += 0.1 + 1.8
        # self.rect.centerx = self.x
        # self.rect.centery = self.y
    