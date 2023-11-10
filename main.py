# Importing the library
import pygame

# Initializing Pygame
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running=True
dt=0

# Colors
border_color = (255, 0, 0)
snake_color = (0, 255, 0)

# Snake attributes
snake_pos=pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
snake_speed=100

# Game starts
while running:
    # If "X" is pressed the game Quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    # Clear the screen of anything from last frame
    screen.fill((0,0,0))
    # Draw the game area
    pygame.draw.rect(screen, border_color, pygame.Rect(250, 250, 500, 500), 2)
    # Draw snake
    pygame.draw.circle(screen, snake_color, snake_pos, 10)

    # Move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_pos.y -= snake_speed*dt
    if keys[pygame.K_a]:
        snake_pos.x -= snake_speed*dt
    if keys[pygame.K_s]:
        snake_pos.y += snake_speed*dt
    if keys[pygame.K_d]:
        snake_pos.x += snake_speed*dt

    if snake_pos.y == 252:
        running=False
    pygame.display.flip()

    dt=clock.tick(60)/1000

pygame.quit()