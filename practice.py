class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printing(self):
        print("Your Name is:"+str(self.name))
        print("Your Age is :"+str(self.age))

p = Person("mahmood",25)
p.printing()
