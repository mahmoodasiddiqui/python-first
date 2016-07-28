class Human():
    def printing(self):
        print("Parent Method is Called")

class Student(Human):
    def printing(self):
        print("Child Method is Called")
        super(Student, self).printing()


s1 = Student()
s1.printing()

#s2 = Human()
#s2.printing()