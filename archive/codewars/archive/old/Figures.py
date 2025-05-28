# implement figures with inheritance etc, circle, triangle, rectangle, square, common methods
class Figure:

    pass


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return Circle.PI * self.radius * self.radius

    def get_perimeter(self):
        return Circle.PI * 2 * self.radius

    def print_circle(self):
        print(f"Circle(radius={self.radius} square={self.get_square()} length={self.get_perimeter()})")



