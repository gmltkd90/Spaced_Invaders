import pygame
from pygame.sprite import Sprite


class Blocker(Sprite):
    def __init__(self, size, color, row, column, ai_settings, screen):
        super(Blocker, self).__init__(self)
        self.height = size
        self.width = size
        self.color = color
        self.image = screen((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.row = row
        self.column = column

    def update(self, keys, *args):
        self.screen.blit(self.image, self.rect)