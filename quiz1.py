count = 0
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        print(str(i)+',')
        count = count+1
print(count)

