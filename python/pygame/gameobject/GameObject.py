import pygame
from Vector import Vector
from math import sin, cos, radians


class GameObject(pygame.sprite.Sprite):
    """
    A special Pygame Sprite object, useful for making games.
    Inspired by the p5.play Sprite object.
    """
    def __init__(self, x, y, width, height, color="white", image=None):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.color = pygame.Color(color)

        if image:
            self.image = pygame.image.load(image)
        else:
            self.image = pygame.Surface([width, height])
            self.image.fill(self.color)

        self.position = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)

        self.rect = self.get_rect_from_pos()

    def update(self):
        """Updates the velocity, position, and rect of the GameObject"""
        self.velocity += self.acceleration
        self.position += self.velocity

        self.rect = self.get_rect_from_pos()

    def get_rect_from_pos(self):
        """Gets rectangle with width, height centered at self.position"""
        top_left = (self.position.x - self.width / 2, self.position.y - self.height / 2)

        return pygame.Rect(top_left, (self.width, self.height))

    # Some other helpful methods!

    def set_speed(self, speed, angle):
        """
        Set the speed of the sprite to be in the given direction.
        Angle is in degrees.
        """
        x = speed * cos(radians(angle))
        y = speed * sin(radians(angle))

        self.velocity = Vector(x, y)

    def add_speed(self, speed, angle):
        """
        Add to the speed of the sprite in the given direction.
        Angle is in degrees.
        """
        x = speed * cos(radians(angle))
        y = speed * sin(radians(angle))

        self.velocity += Vector(x, y)

    def get_speed(self):
        """
        Gets the magnitude of the velocity of the sprite.
        """

        return self.velocity.magnitude()
