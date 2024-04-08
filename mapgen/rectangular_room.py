class RectangularRoom():
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return (center_x, center_y)

    def inner(self):
        """Return the inner area of this room as a 2D array index."""
        return ((self.x1 + 1, self.x2), (self.y1 + 1, self.y2))