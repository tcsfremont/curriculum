import pygame
from Vector import Vector


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color="white"):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.color = pygame.Color(color)

        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)

        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

        self.rect = self.get_rect_from_pos()

    def update(self):
        # Updates the velocity, position, and rect of the GameObject
        self.velocity += self.acceleration
        self.position += self.velocity

        self.rect = self.get_rect_from_pos()

    def get_rect_from_pos(self):
        # Gets rectangle with width, height centered at self.position
        top_left = (self.position.x - self.width / 2, self.position.y - self.height / 2)

        return pygame.Rect(top_left, (self.width, self.height))
