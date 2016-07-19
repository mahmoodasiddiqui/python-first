count = 0
c = []
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        #print(str(i)+',')
        c.append(i)
        count = count+1
for x in range (0,count):
    print(c)
print("Total Numbers = "+str(count))