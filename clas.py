class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        area= self.radius**2*3.14
        return area
a = Circle(3)
print(a.Area())


