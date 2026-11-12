class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def print(self):
        print(f"Point is ({self.x}, {self.y})")

    def __add__(self, p2):
        return Point(self.x + p2.x, self.y + p2.y)

p1 = Point(1, 2)
p2 = Point(10, 20)

p1.print()
p2.print()

p3 = p1 + p2
# p3 = Point(p1.x + p2.x, p1.y + p2.y)
p3.print()

# p3 == Point(11, 22)

# Assignment also overload operator for - (__sub__), *, div