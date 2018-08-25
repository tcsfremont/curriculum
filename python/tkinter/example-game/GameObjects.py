from Vector import Vector
from tkinter import PhotoImage
from random import randint


class GameObject:
    def __init__(self, x, y, width, height, x_vel=0, y_vel=0):
        self.position = Vector(x, y)
        self.velocity = Vector(x_vel, y_vel)

        self.width = width
        self.height = height

    def update(self):
        self.position.add(self.velocity)

    def get_bbox(self):
        top_left = (self.position.x - (self.width / 2), self.position.y - (self.height / 2))
        bottom_right = (self.position.x + (self.width / 2), self.position.y + (self.height / 2))

        return (*top_left, *bottom_right)

    def check_collide(self, platform):
        self_x1, self_y1, self_x2, self_y2 = self.get_bbox()
        platform_x1, platform_y1, platform_x2, platform_y2 = platform.get_bbox()

        if self_x1 < platform_x2:
            if self_x2 > platform_x1:
                if self_y1 < platform_y2:
                    if self_y2 > platform_y1:
                        return True

        return False


class Player(GameObject):
    def __init__(self, x, y, width, height, image_path):
        GameObject.__init__(self, x, y, width, height, x_vel=0, y_vel=0)

        self.image_path = image_path
        self.image = PhotoImage(file=self.image_path)

    def draw(self, game):
        # game.create_image((self.position.x, self.position.y), image=self.image)
        game.create_image((self.position.x, self.position.y), image=self.image)


class Platform(GameObject):
    def __init__(self, x, y, width=140, height=20, color="white"):
        GameObject.__init__(self, x, y, width, height, x_vel=0, y_vel=0)
        self.color = color

    def draw(self, game):
        game.create_rectangle(self.get_bbox(), fill=self.color)


def get_new_platform(game):
    x = randint(0, game.width)
    y = randint(game.height / 2, game.height)

    return Platform(x, y)
