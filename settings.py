class Settings():
    """A Class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 700
        self.bg_color = (0, 0, 0)

        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 2

        # How quickly the game speeds up
        self.speedup_sacle = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize speed setting that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien1_points = None
        #self.alien2_points = 80
        #self.alien3_points = 100

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_sacle
        self.bullet_speed_factor *= self.speedup_sacle
        self.alien_speed_factor *= self.speedup_sacle

        self.alien1_points = int(self.alien1_points * self.score_scale)
        print(self.alien_points)

