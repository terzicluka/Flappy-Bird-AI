import pygame
import os

BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Images","base.png")))
BASE_VELOCITY = 5

class Base:
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = BASE_IMAGE.get_width()
        self.width = BASE_IMAGE.get_width()

    def move(self):
        self.x1 -= BASE_VELOCITY
        self.x2 -= BASE_VELOCITY
        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def draw(self, window):
        window.blit(BASE_IMAGE, (self.x1, self.y))
        window.blit(BASE_IMAGE, (self.x2, self.y))