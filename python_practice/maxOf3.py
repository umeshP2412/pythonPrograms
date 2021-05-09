a = int(input("Give a:"))
b = int(input("Give b:"))
c = int(input("Give c:"))

if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)
