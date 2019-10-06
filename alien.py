import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('image/alien11.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

        self.alien_points = 50

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


class Alien1(Alien):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)
        self.image = pygame.image.load('image/alien33.png')

        self.ai_settings.alien1_points = 10


class Alien2(Alien):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)
        self.image = pygame.image.load('image/alien22.png')

        self.ai_settings.alien1_points = 20


class Alien3(Alien):
    def __init__(self, ai_settings, screen):
        super().__init__(ai_settings, screen)
        self.image = pygame.image.load('image/alien11.png')

        self.ai_settings.alien1_points = 200
