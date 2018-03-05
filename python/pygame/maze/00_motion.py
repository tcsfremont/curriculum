from pygame.locals import *
import pygame

WIDTH = 1000
HEIGHT = 1000

BLACK = (0, 0, 0)
RED = (255, 20, 0)
YELLOW = (255, 255, 0)

speed = 3
px = 100
py = 100
status = "new_game"

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))


player_size = 20

clock = pygame.time.Clock()

while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    pressed = pygame.key.get_pressed()

    if (pressed[K_RIGHT]):
        px = px + speed
    if (pressed[K_LEFT]):
        px = px - speed
    if (pressed[K_UP]):
        py = py - speed
    if (pressed[K_DOWN]):
        py = py + speed
    
    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, (px, py), player_size)

    pygame.display.flip()
