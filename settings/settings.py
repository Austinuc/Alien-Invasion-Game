
class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the games's settings."""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Screen settings
        self.alien_width = self.screen_width // 40
        self.alien_height = self.screen_height // 20

        # Ship settings
        self.ship_speed_factor = 1.5
        
        # self.bg_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.bg_color = (230, 230, 230)
        self.screen_title = "Alien Invasion"

        # Bullet settings
        self.bullet_speed_factor = 2.75
        self.bullet_width = self.screen_width // 400
        self.bullet_height = self.screen_height // 40
        self.bullet_color = 60, 60, 60
        self.bullet_limit = 3