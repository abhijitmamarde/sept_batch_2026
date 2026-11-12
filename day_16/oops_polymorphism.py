# 2nd Pillar of OOPS
# Poly mor phism - same interface multiple actions
# ChessPiece -> PArent Class
# Derived Classes -> pawn, rook, bishop, knight, queen, king
# action of forward / moving / progressing

from abc import abstractmethod

class Shape:
    def __init__(self, point_x, point_y):
        self.x = point_x
        self.y = point_y

    @abstractmethod
    def draw(self):
        pass
        # print("Drawiung basic shape...")

class Circle(Shape):

    def __init__(self, x, y, radious):
        super().__init__(x, y)
        self.radious = radious

    def draw(self):
        print(f"Drawing circle at center: {self.x}, {self.y} with radious: {self.radious}")

class Square(Shape):

    def __init__(self, x, y, side_length):
        super().__init__(x, y)
        # self.x = x
        # self.y = y
        self.side_length = side_length

    def draw(self):
        print(f"Drawing square from bottom left point: {self.x}, {self.y} with length: {self.side_length}")

def draw_all_shapes(shapes):
    for index, shape in enumerate(shapes):
        print(f"Processing the shape {index}...")
        if isinstance(shape, Shape):
            shape.draw()
        else:
            print("Drawing unknown shape...")

s1 = Circle(10, 0, 5)
s2 = Circle(20, 0, 50)
s3 = Square(30, 0, 10)
s4 = Square(40, 0,  2.5)

print("s1 isinnstance of Circle", isinstance(s1, Circle))
print("s1 isinnstance of Square", isinstance(s1, Square))
print("s1 isinnstance of Shape", isinstance(s1, Shape))


print("s3 isinnstance of Circle", isinstance(s3, Circle))
print("s3 isinnstance of Square", isinstance(s3, Square))
print("s3 isinnstance of Shape", isinstance(s3, Shape))


# s1.draw()
# s2.draw()
# s3.draw()
# s4.draw()

s5 = Shape(10, 20)
draw_all_shapes([s1, s2, s3, s4, s5])