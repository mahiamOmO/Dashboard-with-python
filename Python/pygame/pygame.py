import pygame
import random

# Initialize Pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Car Game")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Load images
car_image = pygame.image.load('car.png')
obstacle_image = pygame.image.load('obstacle.png')
car_width = car_image.get_width()
car_height = car_image.get_height()

# Define initial car position
car_x = SCREEN_WIDTH // 2 - car_width // 2
car_y = SCREEN_HEIGHT - car_height - 10

# Define car speed
car_speed = 5

# Obstacle properties
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 7

# Generate initial obstacle
obstacle_x = random.choice([50, 150, 250, 350])
obstacle_y = -obstacle_height

# Main game loop
running = True
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle key presses for car movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 50:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - car_width - 50:
        car_x += car_speed

    # Move the obstacle
    obstacle_y += obstacle_speed

    # Check for collision
    if (car_y < obstacle_y + obstacle_height and
        car_y + car_height > obstacle_y and
        car_x < obstacle_x + obstacle_width and
        car_x + car_width > obstacle_x):
        print("Game Over")
        running = False
    
    # Respawn obstacle if it goes off-screen
    if obstacle_y > SCREEN_HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.choice([50, 150, 250, 350])
        score += 1
        print(f"Score: {score}")

    # Clear the screen
    screen.fill(GREEN)
    
    # Draw road lanes
    pygame.draw.rect(screen, BLACK, (50, 0, 300, SCREEN_HEIGHT))
    pygame.draw.line(screen, WHITE, (150, 0), (150, SCREEN_HEIGHT), 5)
    pygame.draw.line(screen, WHITE, (250, 0), (250, SCREEN_HEIGHT), 5)

    # Draw the car
    screen.blit(car_image, (car_x, car_y))

    # Draw the obstacle
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()