import pygame
import sys

from Vector import Vector

from GameObject import GameObject

pygame.init()

fps = 60
clock = pygame.time.Clock()

game_over = False

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
# END PYGAME INITIALIZATION


# USEFUL FUNCTIONS
def map_range(value, min1, max1, min2, max2):
    return (value - min1) / (max1 - min1) * (max2 - min2) + min2


def text(string, x, y, font_size=12, color="black", font="consolas"):
    text_font = pygame.font.SysFont(font, font_size)
    text_surface = text_font.render(string, True, pygame.color.Color(color))
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


# YOUR CODE HERE

player1score = 0
player2score = 0

ball = GameObject(width / 2, height / 2, 15, 15, color="yellow")
ball.velocity.x = 5

paddle1 = GameObject(40, height / 2, 15, 120, color="cyan")
paddle2 = GameObject(width - 40, height / 2, 15, 120, color="red")

all_sprites = pygame.sprite.Group()
all_sprites.add(ball, paddle1, paddle2)

while not game_over:
    screen.fill((20, 20, 20))

    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # OTHER EVENTS
    if pygame.sprite.collide_rect(ball, paddle1):
        angle = map_range(ball.position.y - paddle1.position.y, -paddle1.height / 2, paddle1.height / 2, -45, 45)
        ball.set_speed(ball.get_speed(), angle)

    if pygame.sprite.collide_rect(ball, paddle2):
        angle = map_range(ball.position.y - paddle2.position.y, -paddle2.height / 2, paddle2.height / 2, 225, 135)
        ball.set_speed(ball.get_speed(), angle)

    if ball.position.y <= ball.height / 2 or ball.position.y >= height - ball.height / 2:
        ball.velocity.y = -ball.velocity.y

    if ball.position.x < -ball.width / 2:
        player2score += 1
        ball.position = Vector(width / 2, height / 2)
        ball.set_speed(5, 180)

    if ball.position.x > width + ball.width / 2:
        player1score += 1
        ball.position = Vector(width / 2, height / 2)
        ball.set_speed(5, 0)

    text(str(player1score), (width / 2) - 200, 50, color="cyan", font_size=32)
    text(str(player2score), (width / 2) + 200, 50, color="red", font_size=32)

    # KEYBOARD INPUT
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_w] and paddle1.position.y >= paddle1.height / 2:
        paddle1.position.y -= 5

    if keys_pressed[pygame.K_s] and paddle1.position.y <= height - paddle1.height / 2:
        paddle1.position.y += 5

    if keys_pressed[pygame.K_UP] and paddle2.position.y >= paddle2.height / 2:
        paddle2.position.y -= 5

    if keys_pressed[pygame.K_DOWN] and paddle2.position.y <= height - paddle2.height / 2:
        paddle2.position.y += 5

    # Update section
    all_sprites.update()

    # DISPLAY SECTION
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)
