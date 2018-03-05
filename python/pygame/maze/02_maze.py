from pygame.locals import *
import pygame
import random
import rgb_colors as rgb


WIDTH = 400
HEIGHT = 400

BLACK = (0, 0, 0)
RED = (255, 20, 0)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

TILECOLORS = (rgb.ALICEBLUE, rgb.SLATEBLUE)

speed = 3
px = 100
py = 100
status = "new_game"
direction = ""
tile_x = 0
tile_y = 0

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Let's read the maze file
maze_file = open("level_1.txt", "r") 

row_count = 15
tile_width = round(WIDTH / row_count)
tile_height = round(HEIGHT / row_count)
player_radius = round(min(tile_width, tile_height) * 0.8 /2) 
player_size = player_radius * 2

walls = []

for row in maze_file.readlines():
    tile_x = 0
    columns = list(row.strip())  # Convert to list and remove newline chars
    for column in columns:
        if column == "*":
            new_wall = pygame.Rect(tile_x, tile_y, tile_width, tile_height)
            walls.append(new_wall)
        if column == "S":
            px = tile_x
            py = tile_y
        tile_x = tile_x + tile_width
    tile_y = tile_y + tile_height

player = pygame.Rect(px, py, player_size, player_size)

clock = pygame.time.Clock()

while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        
    pressed = pygame.key.get_pressed()

    # Note that we are only allowing one direction at a time
    # hence using if / elif
    if (pressed[K_RIGHT]):
        player.x = player.x + speed
        direction = "RIGHT"
    elif (pressed[K_LEFT]):
        player.x = player.x - speed
        direction = "LEFT"
    elif (pressed[K_UP]):
        player.y = player.y - speed
        direction = "UP"
    elif (pressed[K_DOWN]):
        player.y = player.y + speed
        direction = "DOWN"
    
    # Check if the player is about to leave the screen
    # and correct
    if player.right > WIDTH:
        player.right = WIDTH
    if player.left < 0:
        player.left = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if player.top < 0:
        player.top = 0
    
    screen.fill(BLACK)

    # Draw the maze walls
    for wall in walls:
        color = TILECOLORS[random.randint(0, len(TILECOLORS)-1)]
        if player.colliderect(wall):
            color = GRAY
            if direction == "RIGHT":
                player.right = wall.left
            if direction == "LEFT":
                player.left = wall.right
            if direction == "UP":
                player.top = wall.bottom
            if direction == "DOWN":
                player.bottom = wall.top
        pygame.draw.rect(screen, color, wall)

    pygame.draw.circle(screen, YELLOW, player.center, player_radius)

    pygame.display.flip()
