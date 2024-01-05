import pygame
pygame.font.init()
import os

import neat
from GameComponents.bird import Bird
from GameComponents.pipe import Pipe
from GameComponents.base import Base

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 800
FLOOR = 730

PIPE_DISTANCE = 600
SPACE_BETWEEN_PIPES = 160
PIPE_VELOCITY = 8

MAX_GENERATIONS = 2000

BACKGROUND_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("./Images","background.png")))
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")
STATISTICS_FONT = pygame.font.SysFont("arial", 33)
BLACK = (0, 0, 0)

generation = 0

def draw_game(birds, pipes, base, score, generation):
    WINDOW.blit(BACKGROUND_IMAGE, (0,0))

    for pipe in pipes:
        pipe.draw(WINDOW)

    base.draw(WINDOW)
    
    for bird in birds:
        bird.draw(WINDOW)

    score_label = STATISTICS_FONT.render("Score: " + str(score), True, BLACK)
    WINDOW.blit(score_label, (10, 10))

    generation_label = STATISTICS_FONT.render("Current generation: " + str(generation - 1), True, BLACK)
    WINDOW.blit(generation_label, (10, 50))

    birds_alive_label = STATISTICS_FONT.render("Birds alive: " + str(len(birds)), True, BLACK)
    WINDOW.blit(birds_alive_label, (10, 90))

    pygame.display.update()


def fitness_function(genomes, config):
    global generation
    generation += 1
    
    neural_networks = []
    birds = []
    current_genomes = []
    
    for _, genome in genomes:
        genome.fitness = 0
        neural_network = neat.nn.FeedForwardNetwork.create(genome, config)
        neural_networks.append(neural_network)
        birds.append(Bird(230, 350))
        current_genomes.append(genome)

    base = Base(FLOOR)
    pipes = [Pipe(PIPE_DISTANCE, SPACE_BETWEEN_PIPES, PIPE_VELOCITY)]
    score = 0

    clock = pygame.time.Clock()

    while True and len(birds) > 0:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # If pipe passed, show second pipe
        pipe_index = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():  
                pipe_index = 1                                                                 

        # Make move from inputs, and reward bird for staying alive
        for i, bird in enumerate(birds):
            current_genomes[i].fitness += 0.1 # Stayin alive bonus
            bird.move()
            output = neural_networks[i].activate((bird.y, abs(bird.y - pipes[pipe_index].height), abs(bird.y - pipes[pipe_index].bottom)))
            if output[0] > 0.5:
                bird.jump()

        base.move()

        pipes_to_remove = []
        should_add_pipe = False
        for pipe in pipes:
            pipe.move()
            for i, bird in enumerate(birds):
                if pipe.is_collision_detected(bird):
                    current_genomes[i].fitness -= 1 # Punish bird for dying
                    neural_networks.pop(i) # Remove nerual network that crashed
                    current_genomes.pop(i) # Remove genome that crashed
                    birds.pop(i) # Remove bird that crashed

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                pipes_to_remove.append(pipe)

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                should_add_pipe = True

        # Since pipe should be passed, update the score and reward bird for passing
        if should_add_pipe:
            score += 1
            for genome in current_genomes:
                genome.fitness += 5
            pipes.append(Pipe(PIPE_DISTANCE, SPACE_BETWEEN_PIPES, PIPE_VELOCITY))

        for pipe_to_remove in pipes_to_remove:
            pipes.remove(pipe_to_remove)

        # Punish bird for hitting the ground or flying too high
        for i, bird in enumerate(birds):
            if bird.y + bird.current_image.get_height() - 10 >= FLOOR or bird.y < -50:
                neural_networks.pop(i) # Remove nerual network that crashed
                current_genomes.pop(i) # Remove genome that crashed
                birds.pop(i) # Remove bird that crashed

        draw_game(birds, pipes, base, score, generation)


def main(configuration_path):
    configuration = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         configuration_path)
    
    population = neat.Population(configuration)

    population.add_reporter(neat.StdOutReporter(True))
    statistics = neat.StatisticsReporter()
    population.add_reporter(statistics)

    winner = population.run(fitness_function, MAX_GENERATIONS)

    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    local_directory = os.path.dirname(__file__)
    configuration_path = os.path.join(local_directory, 'config-feedforward.txt')
    main(configuration_path)