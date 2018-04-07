# Pygame Example

import pygame

pygame.init()

clock = pygame.time.Clock()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

LINK_IMG = pygame.image.load("link.png").convert()

all_sprites = pygame.sprite.Group()

class SpriteSheet:
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey((0, 0, 0))

        return image

link_spritesheet = SpriteSheet("link_spritesheet.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = LINK_IMG
        self.rect = self.image.get_rect()

        self.rect.center = (width / 2, height / 2)

        self.direction = "down"
        self.move_tick = 0

    def set_img(self, row, col):
        # sheet is 288 x 256

        img_width = 288 / 12
        img_height = 256 / 8

        x = row * img_width
        y = col * img_height

        self.image = link_spritesheet.get_image(x, y, img_width, img_height)
        self.rect = self.image.get_rect()

        self.rect.center = (width / 2, height / 2)
        

link = Player()
link.set_img(0, 0)

all_sprites.add(link)

# Game Loop

game_over = False

while not game_over:

    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        link.move("left")
    

    # screen.fill((0, 255, 0))
    all_sprites.draw(screen)
    
    pygame.display.flip()
    
                
pygame.quit()
quit()
