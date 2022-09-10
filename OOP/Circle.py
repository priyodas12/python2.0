class Circle():
    pi = 3.14

    def __init__(self, radious=10):
        self.radious = radious

    def get_area(self):
        return self.pi*self.radious*self.radious


circle = Circle()
print(circle.get_area())
