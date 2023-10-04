import pygame
import os
import bird as bird_module
import position

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
BIRD_START_POSITION = position.Position(200, 200)

BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Project/Images", "background.png")))

def draw_background(window, bird):
    window.blit(BACKGROUND_IMAGE, (0, 0))
    bird.draw(window)
    pygame.display.update()
    
def main():
    bird = bird_module.Bird(BIRD_START_POSITION)
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    
    run = True
    
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        bird.move()        
        draw_background(window, bird)
        
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()