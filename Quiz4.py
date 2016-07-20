msg = "hello world ! 123"
digit =0
letter =0
for i in msg:
    if i.isdigit():
        digit = digit+1
    elif i.isalpha():
        letter = letter+1
print("Digits :"+str(digit))
print("Letter :"+str(letter))





