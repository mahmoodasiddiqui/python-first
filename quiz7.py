import random

def myrand():
    mini = int(input("Enter Min Range"))
    maxi = int(input("Enter Max Range"))
    range = (maxi - mini + 1)
    ans = (random.random() * range + mini)
    print(int(ans))
    print(ans)

