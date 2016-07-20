msg = "hello world ! 123"
digit =0
letter =0
special=0
for i in msg:
    if i.isdigit():
        digit = digit+1
    elif i.isalpha():
        letter = letter+1
    else:
        special=special+1
print("Digits :"+str(digit))
print("Letter :"+str(letter))
print("Special :"+str(special))





