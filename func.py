def name():
    n=input("Whats Your Name?")
    print("Your Name Is: "+n)
name()

def name(n2):
    print("Your Name Is: " + n2)
n2=input("Whats Your Name?")
name(n2)

def tname():
    n = input("Whats Your Name?")
    return n.title()
print("Your Name Is:"+tname())