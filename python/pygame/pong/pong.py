import pygame
import sys

from Paddle import Paddle
from Ball import Ball
from Vector import Vector

from GameObject import GameObject

pygame.init()

fps = 60
clock = pygame.time.Clock()

game_over = False

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

ball = GameObject(width / 2, height / 2, 15, 15)
ball.velocity.x = 4

paddle1 = GameObject(40, height / 2, 15, 200)
paddle2 = GameObject(width - 40, height / 2, 15, 200)

all_sprites = pygame.sprite.Group()
all_sprites.add(ball, paddle1, paddle2)

while not game_over:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_w]:
        paddle1.position.y -= 5

    if keys_pressed[pygame.K_s]:
        paddle1.position.y += 5

    if keys_pressed[pygame.K_UP]:
        paddle2.position.y -= 5

    if keys_pressed[pygame.K_DOWN]:
        paddle2.position.y += 5

    for sprite in all_sprites:
        sprite.update()

    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)
