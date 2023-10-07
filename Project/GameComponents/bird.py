import pygame
import os

BIRD_DOWNFLAP_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Project/Images","birdDownFlap.png")))
BIRD_MIDFLAP_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Project/Images","birdMidFlap.png")))
BIRD_UPFLAP_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Project/Images","birdUpFlap.png")))
IMAGES = [BIRD_DOWNFLAP_IMAGE, BIRD_MIDFLAP_IMAGE, BIRD_UPFLAP_IMAGE]

MAX_ROTATION = 25
ROTATION_VELOCITY = 20
ANIMATION_TIME = 5

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y
        self.image_count = 0
        self.current_image = IMAGES[0]

    def jump(self):
        self.velocity = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1
        displacement = self.__calculate_displacement()
        self.__update_y_with_displacement(displacement)
        self.__rotate_bird(displacement)

    def draw(self, window):
        self.image_count += 1
        
        if self.image_count <= ANIMATION_TIME:
            self.current_image = IMAGES[0]
        elif self.image_count <= ANIMATION_TIME*2:
            self.current_image = IMAGES[1]
        elif self.image_count <= ANIMATION_TIME*3:
            self.current_image = IMAGES[2]
        elif self.image_count <= ANIMATION_TIME*4:
            self.current_image = IMAGES[1]
        elif self.image_count == ANIMATION_TIME*4 + 1:
            self.current_image = IMAGES[0]
            self.image_count = 0

        if self.tilt <= -80:
            self.current_image = IMAGES[1]
            self.image_count = ANIMATION_TIME*2


        blitRotateCenter(window, self.current_image, (self.x, self.y), self.tilt)

    def get_mask(self):
        return pygame.mask.from_surface(self.current_image)

    def __calculate_displacement(self):
        displacement = self.velocity*self.tick_count + 1.5*self.tick_count**2

        if displacement >= 16:
            displacement = 16

        if displacement < 0:
            displacement -= 2
            
        return displacement
    
    def __update_y_with_displacement(self, displacement):
        self.y = self.y + displacement
        
    def __rotate_bird(self, displacement):
        if displacement < 0 or self.y < self.height + 50:  # tilt up
            if self.tilt < MAX_ROTATION:
                self.tilt = MAX_ROTATION
        else:  # tilt down
            if self.tilt > -90:
                self.tilt -= ROTATION_VELOCITY

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect.topleft)