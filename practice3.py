class human(object):
    def __eq__(self,age):
        #print("__eq__ called")
        return self.value == age

a=human()
a.value = 3
b=human()
b.value = 4
print("a.value and b.value is equal")
print(a==b)

