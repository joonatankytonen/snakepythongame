# Importing the library
import pygame

# Initializing Pygame
pygame.init()
Screen_Height=1000
Screen_Width=1000
screen = pygame.display.set_mode((Screen_Height, Screen_Width))
clock = pygame.time.Clock()
running=True
dt=0
points=[(250,250),(250, 750), (750,750), (750, 250)]

# Colors
border_color = (255, 0, 0)
snake_color = (0, 255, 0)

# Snake
snake=pygame.Rect((Screen_Height/2),(Screen_Width/2),25,25)

# Map
left=pygame.Rect(250, 250, 2, 500)
top=pygame.Rect(250,250,500,2)
right=pygame.Rect(750, 250, 2, 500)
bottom=pygame.Rect(250, 750, 500, 2)


# Game starts
while running:
    # If "X" is pressed the game Quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


    # Clear the screen of anything from last frame
    screen.fill((0,0,0))
    # Draw the map
    pygame.draw.rect(screen, border_color, left)
    pygame.draw.rect(screen, border_color, top)
    pygame.draw.rect(screen, border_color, right)
    pygame.draw.rect(screen, border_color, bottom)
    #asd = pygame.draw.lines(screen, border_color, False, points, 2)
    # Draw snake
    pygame.draw.rect(screen, snake_color, snake)

    # Move snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake.move_ip(0,-1)
    elif keys[pygame.K_a]:
        snake.move_ip(-1,0)
    elif keys[pygame.K_s]:
        snake.move_ip(0,1)
    elif keys[pygame.K_d]:
        snake.move_ip(1,0)

    if snake.colliderect(left):
        running = False
    elif snake.colliderect(top):
        running = False
    elif snake.colliderect(right):
        running = False
    elif snake.colliderect(bottom):
        running = False

    pygame.display.flip()

    # Run game on 60fps
    dt=clock.tick(60)/1000

pygame.quit()