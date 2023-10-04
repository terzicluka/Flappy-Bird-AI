import pygame
import os

class Pipe:
    BASE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Project/Images", "base.png")))
    
    VELOCITY = 5
    WIDTH = BASE_IMAGE.get_width()
    
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        
    def move(self):
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY
        
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH
    
    def draw(self, window):
        window.blit(self.BASE_IMAGE, (self.x1, self.y))
        window.blit(self.BASE_IMAGE, (self.x2, self.y))