from pygame.locals import *
import pygame

WIDTH = 500
HEIGHT = 500

BLACK = (0, 0, 0)
RED = (255, 20, 0)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

speed = 3
px = 100
py = 100
status = "new_game"

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Let's keep track of the walls
walls = []

player_size = 20

# Add a few walls for testing
tile1 = pygame.Rect(100, 150, player_size * 2, player_size * 2)
walls.append(tile1)
tile2 = pygame.Rect(200, 150, player_size * 2, player_size * 2)
walls.append(tile2)
print(walls)

# Let's add a box around the player that we can use for motion and collision
# player_size is the radius of a circle, so we multiply by 2
player = pygame.Rect(px, py, player_size * 2, player_size * 2)

clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    pressed = pygame.key.get_pressed()

    if (pressed[K_RIGHT]):
        player.x = player.x + speed
    if (pressed[K_LEFT]):
        player.x = player.x - speed
    if (pressed[K_UP]):
        player.y = player.y - speed
    if (pressed[K_DOWN]):
        player.y = player.y + speed
    
    # Check if the player is about to leave the screen
    # and correct
    if player.right > WIDTH:
        player.right = WIDTH
    if player.center[0] < 0:
        player.center[0] = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if player.top < 0:
        player.top = 0

    screen.fill(BLACK)
    # Draw and Check for collisions with walls
    # We're just changing the color of the walls when there's collision
    for wall in walls:
        color = RED
        if player.colliderect(wall):
            color = GRAY
        pygame.draw.rect(screen, color, wall)
    
    
    #pygame.draw.rect(screen, RED, tile2)
    pygame.draw.circle(screen, YELLOW, player.center, player_size)

    pygame.display.flip()
