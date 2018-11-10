from GameObject import GameObject


class Ball(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y, 50, 50, color=(0, 255, 255))
