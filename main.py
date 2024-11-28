import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chicken Clicker")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
score = 0
clicks_per_click = 1

# Load chicken image
chicken_img = pygame.image.load(os.path.join("assets", "chicken.png"))
chicken_img = pygame.transform.scale(chicken_img, (200, 200))
chicken_rect = chicken_img.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

# Font setup
font = pygame.font.Font(None, 36)

def draw_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if chicken_rect.collidepoint(event.pos):
                score += clicks_per_click
                # Add a simple animation effect
                chicken_rect.y += 5
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if chicken_rect.collidepoint(event.pos):
                chicken_rect.y -= 5

    # Draw everything
    screen.fill(WHITE)
    screen.blit(chicken_img, chicken_rect)
    draw_score()
    
    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
