ans = 0
def facto(x):
    if x == 0:
        return 1
    return x * facto(x - 1)

x=int(input("Enter The Number"))
ans = facto(x)
print(ans)
