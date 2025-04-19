import pygame
import time
import random

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Load sounds
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)  # Loop background music
eat_sound = pygame.mixer.Sound("eat.wav")

# Set up display
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🐍 Snake Game with Sound')

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

# Clock & font
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 24)

# Draw snake
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))

def game_loop():
    snake = [[100, 50], [80, 50], [60, 50]]
    direction = 'RIGHT'
    change_to = direction
    food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
    score = 0
    speed = 10

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to
        head_x, head_y = snake[0]

        if direction == 'UP':
            head_y -= CELL_SIZE
        elif direction == 'DOWN':
            head_y += CELL_SIZE
        elif direction == 'LEFT':
            head_x -= CELL_SIZE
        elif direction == 'RIGHT':
            head_x += CELL_SIZE

        new_head = [head_x, head_y]
        snake.insert(0, new_head)

        # Collision detection
        head_rect = pygame.Rect(head_x, head_y, CELL_SIZE, CELL_SIZE)
        food_rect = pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE)

        if head_rect.colliderect(food_rect):
            score += 1
            speed += 0.5
            eat_sound.play()  # Play eating sound
            food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
        else:
            snake.pop()

        # Game over conditions
        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in snake[1:]):
            msg = font.render("💀 Game Over! Score: " + str(score), True, WHITE)
            screen.blit(msg, [WIDTH // 4, HEIGHT // 2])
            pygame.display.update()
            time.sleep(2)
            running = False

        # Draw food and snake
        pygame.draw.rect(screen, RED, food_rect)
        draw_snake(snake)

        # Display score
        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, [10, 10])

        pygame.display.update()
        clock.tick(int(speed))

    pygame.quit()

# Start game
game_loop()
