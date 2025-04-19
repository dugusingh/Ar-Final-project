import pygame
import random

# Initialize
pygame.init()
pygame.mixer.init()

# Load sounds
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)  # Loop background music

catch_sound = pygame.mixer.Sound("catch.wav")

# Window settings
WIDTH, HEIGHT = 500, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

# Basket (player)
basket_width, basket_height = 100, 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 7

# Ball
ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 0
ball_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 40)

# Game loop flag
run = True
clock = pygame.time.Clock()

while run:
    clock.tick(30)  # 30 FPS
    win.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Ball falling
    ball_y += ball_speed

    # Collision detection
    if basket_y < ball_y + ball_radius < basket_y + basket_height:
        if basket_x < ball_x < basket_x + basket_width:
            score += 1
            catch_sound.play()  # Play catch sound
            ball_y = 0
            ball_x = random.randint(ball_radius, WIDTH - ball_radius)

    # Reset ball if missed
    if ball_y > HEIGHT:
        ball_y = 0
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)

    # Draw basket
    pygame.draw.rect(win, BROWN, (basket_x, basket_y, basket_width, basket_height))

    # Draw ball
    pygame.draw.circle(win, RED, (ball_x, ball_y), ball_radius)

    # Draw score
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    win.blit(score_text, (10, 10))

    # Update screen
    pygame.display.update()

pygame.quit()
