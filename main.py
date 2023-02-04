import pygame
import sys
from snake import Snake

pygame.init()

width, height = 500, 500

clock = pygame.time.Clock()
current_time = pygame.time.get_ticks()

display = pygame.display.set_mode((width, height))
display.fill("#5CC8FF")
pygame.display.update()
pygame.display.set_caption("Snake")

snake = Snake(display)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = "UP"
            if event.key == pygame.K_DOWN:
                snake.direction = "DOWN"
            if event.key == pygame.K_LEFT:
                snake.direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                snake.direction = "RIGHT"

    # Run code only every 0.2 second
    elapsed_time = pygame.time.get_ticks() - current_time
    if elapsed_time >= 200: # Time in milliseconds
        current_time = pygame.time.get_ticks()
        # Code to run every 0.2 second goes here

        display.fill("#5CC8FF")

        snake.update()
        snake.draw()
        
        pygame.display.update()
        

    