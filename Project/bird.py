import pygame
import os
import position

class Bird:
    DOWN_FLAP_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Project/Images", "birdDownFlap.png")))
    MID_FLAP_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Project/Images", "birdMidFlap.png")))
    UP_FLAP_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Project/Images", "birdUpFlap.png")))
    
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5
    
    def __init__(self, position: position.Position):
        self.position = position
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.position.y
        self.image_count = 0
        self.current_image = self.DOWN_FLAP_IMAGE
    
    def jump(self):
        self.__reset_tick()
        self.__move_up()
    
    def move(self):
        self.tick_count += 1
        displacement = self.__calculate_displacement()        
        self.position.y += displacement
        self.__rotate_bird(displacement)
        
    def draw(self, window):
        self.__calculate_new_image()
        rotated_image = pygame.transform.rotate(self.current_image, self.tilt)
        new_rectangle = rotated_image.get_rect(center=self.current_image.get_rect(topleft=(self.position.x, self.position.y)).center)
        window.blit(rotated_image, new_rectangle.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.current_image)
    
    def __reset_tick(self):
        self.tick_count = 0
        
    def __move_up(self):
        self.position.y -= 10.5
        self.height = self.position.y
        
    def __calculate_displacement(self):
        current_displacement = self.velocity * self.tick_count + 1.5 * self.tick_count ** 2
        if current_displacement >= 16:
            current_displacement = 16
        elif current_displacement < 0:
            current_displacement -= 3
        return current_displacement

    def __rotate_bird(self, displacement):
        if displacement < 0 or self.position.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROTATION_VELOCITY
    
    def __calculate_new_image(self):
        self.image_count += 1
        
        if self.image_count < self.ANIMATION_TIME:
            self.current_image = self.DOWN_FLAP_IMAGE
        elif self.image_count < self.ANIMATION_TIME * 2:
            self.current_image = self.MID_FLAP_IMAGE
        elif self.image_count < self.ANIMATION_TIME * 3:
            self.current_image = self.UP_FLAP_IMAGE
        elif self.image_count < self.ANIMATION_TIME * 4:
            self.current_image = self.MID_FLAP_IMAGE
        elif self.image_count < self.ANIMATION_TIME * 4 + 1:
            self.current_image = self.DOWN_FLAP_IMAGE
            self.image_count = 0
        
        if self.tilt <= -80:
            self.current_image = self.MID_FLAP_IMAGE
            self.image_count = self.ANIMATION_TIME * 2