# A vector with all the operations we need for a game


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def multiply(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def as_list(self):
        return [self.x, self.y]
