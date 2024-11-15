import pygame
import time
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake block size
block_size = 20
snake_speed = 10

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Display the score
def display_score(score):
    value = score_font.render(f"Score: {score}", True, green)
    screen.blit(value, [10, 10])

# Draw the snake
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, blue, [block[0], block[1], block_size, block_size])

# Display a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Game Loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = width / 2
    y1 = height / 2

    # Movement direction
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_list = []
    length_of_snake = 1

    # Food position
    food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(black)
            message("Game Over! Press Q to Quit or C to Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for collisions with walls
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        pygame.draw.rect(screen, green, [food_x, food_y, block_size, block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for collisions with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if food is eaten
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()