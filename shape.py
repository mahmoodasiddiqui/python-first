class Shape():
    def __init__(self):
       a = 0

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,l):
        self.length = l

    def area(self):
        area = self.length*self.length
        return area
sq = Square(4)
print(sq.area())
