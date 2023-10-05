import pygame
import os
import bird as bird_module
import pipe as pipe_module
import base as base_module
import difficulty_constants
import position
pygame.font.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
BIRD_START_POSITION = position.Position(230, 350)
BASE_HEIGHT = 730

SCORE_FONT = pygame.font.SysFont("comicsans", 50)

BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Project/Images", "background.png")))

def draw_game(window, score, bird, pipes, base):
    window.blit(BACKGROUND_IMAGE, (0, 0))
    
    text = SCORE_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    
    for pipe in pipes:
        pipe.draw(window)
        
    bird.draw(window)
    base.draw(window)
    
    window.blit(text, (WINDOW_WIDTH - 10 - text.get_width(), 10))
    
    pygame.display.update()
    
def main():
    score = 0
    
    bird = bird_module.Bird(BIRD_START_POSITION)
    base = base_module.Base(BASE_HEIGHT)
    pipes = [pipe_module.Pipe(difficulty_constants.PIPE_DISTANCE)]
    
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    
    run = True
    
    while run:
        clock.tick(difficulty_constants.TICKS_PER_SECOND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pipes_to_remove = []
        should_add_pipe = False
        for pipe in pipes:
            if pipe.is_collision_detected(bird):
                pass
            if pipe.x + pipe.pipe_top.get_width() < 0:
                pipes_to_remove.append(pipe)
            if not pipe.passed and pipe.x < bird.position.x:
                pipe.passed = True
                should_add_pipe = True
            pipe.move()
            
        if should_add_pipe:
            score += 1
            pipes.append(pipe_module.Pipe(difficulty_constants.PIPE_DISTANCE))
            should_add_pipe = False
        
        for pipe_to_remove in pipes_to_remove:
            pipes.remove(pipe_to_remove)
        
        if bird.position.y + bird.current_image.get_height() >= BASE_HEIGHT:
            pass
            
        base.move()
        #bird.move()        
        draw_game(window, score, bird, pipes, base)
        
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()