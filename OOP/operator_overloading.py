# Python allows us to override operators like 
# +, -, *, / using special methods (dunder methods).

class Point:
    """Represents a coordinate in 2D"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


print(Point.__doc__)

p1 = Point(3, 5)
p2 = Point(6, 7)

p3 = p1 + p2
print(p3)

print(p2.__doc__)
