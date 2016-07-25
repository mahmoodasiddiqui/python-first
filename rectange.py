class rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        a= self.length*self.width
        return a
b = rectangle(3,4)
x = b.area()
print(x)


