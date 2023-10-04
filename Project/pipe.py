import pygame
import random
import os
import bird as bird_module

class Pipe:
    PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Project/Images", "pipe.png")))
    
    SPACE_BETWEEN_PIPES = 200
    VELOCITY = 5
    
    def __init__(self, x):
        self.x = x
        
        self.pipe_top = pygame.transform.flip(self.PIPE_IMAGE, False, True)
        self.pipe_bottom = self.PIPE_IMAGE
        
        self.passed = False
        
        self.calculate_height()
        self.calculate_position()
        
    def move(self):
        self.x -= self.VELOCITY
    
    def draw(self, window):
        window.blit(self.pipe_top, (self.x, self.top))
        window.blit(self.pipe_bottom, (self.x, self.bottom))
        
    def is_collision_detected(self, bird: bird_module.Bird):
        bird_mask = bird.get_mask()
        # Needs calculation of mask for the pipes since there are transparent pixels
        top_mask = pygame.mask.from_surface(self.pipe_top)
        bottom_mask = pygame.mask.from_surface(self.pipe_bottom)
        
        top_offset = (self.x - bird.position.x, self.top - round(bird.position.y))
        bottom_offset = (self.x - bird.position.x, self.bottom - round(bird.position.y))
        
        bottom_point = bird_mask.overlap(bottom_mask, bottom_offset)
        top_point = bird_mask.overlap(top_mask, top_offset)
        
        return top_point or bottom_point
        
    def __calculate_height(self):
        self.height = random.randrange(50, 450)
    
    def __calculate_position(self):
        self.top = self.height - self.pipe_top.get_height()
        self.bottom = self.height + self.SPACE_BETWEEN_PIPES