import pygame
import sys

from Vector import Vector
from GameObject import GameObject

import random

pygame.init()

fps = 60
frame = 0
clock = pygame.time.Clock()

game_over = False

width, height = 640, 600
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


def get_image(posx, posy, width, height, sprite_sheet):
    """Extracts image from sprite sheet.
    Source: https://www.reddit.com/r/pygame/comments/23u11o/how_do_i_break_up_a_sprite_sheet/ch0nnhu"""

    image = pygame.Surface([width, height])
    image.blit(sprite_sheet, (0, 0), (posx, posy, width, height))
    image.set_colorkey((0, 0, 0))

    return image


# USEFUL COLORS
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 192, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BACKGROUND_COLOR = BLACK


# Dr. Mario in Pygame!

PILL_SIZE = 20

# Sprite Images
sprite_sheet = pygame.image.load("dr_mario_sprites.png")

red_top = get_image(0, 0, 20, 20, sprite_sheet)
red_bottom = get_image(0, 20, 20, 20, sprite_sheet)
red_left = get_image(0, 40, 20, 20, sprite_sheet)
red_right = get_image(0, 60, 20, 20, sprite_sheet)
red_single = get_image(0, 80, 20, 20, sprite_sheet)
red_circle = get_image(0, 100, 20, 20, sprite_sheet)

yellow_top = get_image(20, 0, 20, 20, sprite_sheet)
yellow_bottom = get_image(20, 20, 20, 20, sprite_sheet)
yellow_left = get_image(20, 40, 20, 20, sprite_sheet)
yellow_right = get_image(20, 60, 20, 20, sprite_sheet)
yellow_single = get_image(20, 80, 20, 20, sprite_sheet)
yellow_circle = get_image(20, 100, 20, 20, sprite_sheet)

blue_top = get_image(40, 0, 20, 20, sprite_sheet)
blue_bottom = get_image(40, 20, 20, 20, sprite_sheet)
blue_left = get_image(40, 40, 20, 20, sprite_sheet)
blue_right = get_image(40, 60, 20, 20, sprite_sheet)
blue_single = get_image(40, 80, 20, 20, sprite_sheet)
blue_circle = get_image(40, 100, 20, 20, sprite_sheet)

virus_sprite_sheet = pygame.image.load("viruses_sprites.png")

red_virus1 = get_image(0, 0, 20, 20, virus_sprite_sheet)
red_virus2 = get_image(0, 20, 20, 20, virus_sprite_sheet)

yellow_virus1 = get_image(0, 40, 20, 20, virus_sprite_sheet)
yellow_virus2 = get_image(0, 60, 20, 20, virus_sprite_sheet)

blue_virus1 = get_image(0, 80, 20, 20, virus_sprite_sheet)
blue_virus2 = get_image(0, 100, 20, 20, virus_sprite_sheet)

background_image = pygame.image.load("background.png")

# Pill area, top left: (240, 200)
# Pill area, bottom right: (400, 520)


class Pill(GameObject):
    def __init__(self, x, y, color1, color2):
        self.color1 = color1
        self.color2 = color2

        # Construct the image
        if color1 == "red":
            self.left_image = red_left
        elif color1 == "yellow":
            self.left_image = yellow_left
        else:
            self.left_image = blue_left

        if color2 == "red":
            self.right_image = red_right
        elif color2 == "yellow":
            self.right_image = yellow_right
        else:
            self.right_image = blue_right

        image = pygame.Surface((PILL_SIZE * 2, PILL_SIZE))
        image.blit(self.left_image, (0, 0), (0, 0, 20, 20))
        image.blit(self.right_image, (20, 0), (0, 0, 20, 20))
        image.set_colorkey((0, 0, 0))

        GameObject.__init__(self, x, y, PILL_SIZE * 2, PILL_SIZE)
        self.image = image

    def drop(self):
        self.position.y += PILL_SIZE

    def rotate(self):
        self.width, self.height = self.height, self.width
        self.image = pygame.Surface((self.width, self.height))

        if self.height > self.width:  # Vertical
            # Construct the image
            if self.color1 == "red":
                self.left_image = red_bottom
            elif self.color1 == "yellow":
                self.left_image = yellow_bottom
            else:
                self.left_image = blue_bottom

            if self.color2 == "red":
                self.right_image = red_top
            elif self.color2 == "yellow":
                self.right_image = yellow_top
            else:
                self.right_image = blue_top

            self.image.blit(self.right_image, (0, 0), (0, 0, 20, 20))
            self.image.blit(self.left_image, (0, 20), (0, 0, 20, 20))

            self.position.x -= PILL_SIZE / 2
            self.position.y -= PILL_SIZE / 2

        else:  # Horizontal
            self.color1, self.color2 = self.color2, self.color1

            # Construct the image
            if self.color1 == "red":
                self.left_image = red_left
            elif self.color1 == "yellow":
                self.left_image = yellow_left
            else:
                self.left_image = blue_left

            if self.color2 == "red":
                self.right_image = red_right
            elif self.color2 == "yellow":
                self.right_image = yellow_right
            else:
                self.right_image = blue_right

            self.image.blit(self.left_image, (0, 0), (0, 0, 20, 20))
            self.image.blit(self.right_image, (20, 0), (0, 0, 20, 20))

            self.position.x += PILL_SIZE / 2
            self.position.y += PILL_SIZE / 2

        self.image.set_colorkey((0, 0, 0))


class Virus(GameObject):
    def __init__(self, x, y, color):
        GameObject.__init__(self, x, y, PILL_SIZE, PILL_SIZE)

        self.color = color

        self.frame = 0

        if self.color == "red":
            self.image = red_virus1
            self.images = [red_virus1, red_virus2]
        elif self.color == "yellow":
            self.image = yellow_virus1
            self.images = [yellow_virus1, yellow_virus2]
        else:
            self.image = blue_virus1
            self.images = [blue_virus1, blue_virus2]

        self.image.set_colorkey((0, 0, 0))

    def animate(self):
        self.frame = (self.frame + 1) % 2
        self.image = self.images[self.frame]
        self.image.set_colorkey((0, 0, 0))


def spawn_pill():
    colors = ["red", "yellow", "blue"]
    color1 = random.choice(colors)
    color2 = random.choice(colors)

    return Pill(width / 2, 210, color1, color2)


def grid_to_screen(row, column):
    x = 240 + (PILL_SIZE * column) + (PILL_SIZE / 2)
    y = 200 + (PILL_SIZE * row) + (PILL_SIZE / 2)

    return x, y


def generate_level(difficulty):
    prob = map_range(difficulty, 1, 20, 0.1, 0.8)
    min_depth = int(map_range(difficulty, 1, 20, 10, 2))

    print(prob, min_depth)

    # grid[row][col]

    grid = []
    viruses = []

    for y in range(16):
        row = []
        for x in range(8):
            if y > min_depth and random.random() < prob:
                color = random.choice(["red", "yellow", "blue"])
                virus = Virus(*grid_to_screen(y, x), color)

                row.append(virus)
                viruses.append(virus)
            else:
                row.append(None)
        grid.append(row)

    return grid, viruses


current_pill = None

all_sprites = pygame.sprite.Group()
grid, viruses = generate_level(20)
# grid[row][col]

all_sprites.add(*viruses)

while not game_over:
    # Draw background
    screen.blit(background_image, (0, 0), (0, 0, width, height))

    # EVENT LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_SPACE:
                if current_pill:
                    current_pill.rotate()
            if event.key == pygame.K_s:
                current_pill = spawn_pill()
                all_sprites.add(current_pill)

    # OTHER EVENTS
    if frame % 30 == 0:
        if current_pill:
            current_pill.drop()
        for virus in viruses:
            virus.animate()

    # KEYBOARD INPUT
    keys_pressed = pygame.key.get_pressed()

    # Update section
    all_sprites.update()

    # DISPLAY SECTION
    all_sprites.draw(screen)

    frame += 1
    pygame.display.flip()
    clock.tick(fps)
