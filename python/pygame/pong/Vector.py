class Vector:
    """A 2D vector used for moving things around."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __str__(self):
        return "Vector(" + str(self.x) + ", " + str(self.y) + ")"

    def magnitude(self):
        return (self.x * self.x + self.y * self.y) ** (1 / 2)
