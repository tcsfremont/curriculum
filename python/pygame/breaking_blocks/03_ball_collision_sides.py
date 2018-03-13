""" Base window for breakout game using pygame."""
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


WIDTH = 800
HEIGHT = 600

BALL_RADIUS = 8
BALL_DIAMETER = BALL_RADIUS * 2

# Add velocity component as a list with X and Y values
ball_velocity = [10, -10]

def move_ball(ball):
    """Change the location of the ball using velocity and direction."""

    ball.left = ball.left + ball_velocity[0]
    ball.top = ball.top + ball_velocity[1]

    # Check if ball is going beyond the window 
    if ball.left <= 0:
        ball.left = 0
        ball_velocity[0] = -ball_velocity[0]
    elif ball.left > WIDTH - BALL_DIAMETER:
        # Take diameter into account because we are checking the
        # left edge of the ball
        ball.left = WIDTH - BALL_DIAMETER
        ball_velocity[0] = -ball_velocity[0]

    if ball.top <= 0:
        ball.top = 0
        ball_velocity[1] = -ball_velocity[1]
    elif ball.top > HEIGHT - BALL_DIAMETER:
        # Take diameter into account because we are checking the
        # top edge of the ball
        ball.top = HEIGHT - BALL_DIAMETER
        ball_velocity[1] = -ball_velocity[1]

    return ball

def game():
    """Main function for the game."""


    # Define the ball as a square box the size of the ball
    # We can use this to check collision later
    ball = pygame.Rect(300, HEIGHT - BALL_DIAMETER,BALL_DIAMETER,BALL_DIAMETER)
    
    # Initialize pygame 
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Breaking Blocks")
    clock = pygame.time.Clock()

    # Game Loop
    while True:
        # Set max frames per second
        clock.tick(20)

        # Fill the screen on every update
        screen.fill(BLACK)

        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Move ball
        ball = move_ball(ball)

         # Draw ball
        pygame.draw.circle(screen, WHITE, (ball.left + BALL_RADIUS, ball.top + BALL_RADIUS), BALL_RADIUS)

        # Paint and refresh the screen
        pygame.display.flip()



if __name__ == "__main__":
    game()