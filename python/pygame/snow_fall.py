import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (400, 400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snowfall")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Let's create an empty array
snowflakes = []

# Create 50 snowflakes at random x,y locations
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snowflakes.append([x, y])


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Screen-clearing code goes here

    # Here, we clear the screen to the color of choice.
    screen.fill(BLACK)

    # --- Drawing code should go here
    for i in range(len(snowflakes)):
        # Draw the snowflake
        pygame.draw.circle(screen, WHITE, snowflakes[i], 2)

        # Move the y coordinate by 1 pixel
        snowflakes[i][1] += 1

        # check if the flake left the bottom of the screen
        # and generate a new random one
        if snowflakes[i][1] > 400:
            new_y = random.randrange(-50, -10)
            snowflakes[i][1] = new_y
            new_x = random.randrange(0, 400)
            snowflakes[i][0] = new_x

    # --- Game logic should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
