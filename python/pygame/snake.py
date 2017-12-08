"""
Pygame based game.

Snake Game

"""
import pygame

# Define colors here
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3

# Set initial speed
x_change = segment_width + segment_margin
y_change = 0

# Create a class to build a snake segment
#
class Segment(pygame.sprite.Sprite):

    """ Constructor method."""
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Initialize pygame library
pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snaaaaaaaaaake")

all_sprites_list = pygame.sprite.Group()

# Initial snake
snake_segments = []
for i in range(15):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    all_sprites_list.add(segment)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin) * 1
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin) * 1

    old_segment = snake_segments.pop()
    all_sprites_list.remove(old_segment)

    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)

    snake_segments.insert(0, segment)
    all_sprites_list.add(segment)

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to black. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    # --- Drawing code should go here
    all_sprites_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(5)

# Close the window and quit.
pygame.quit()
