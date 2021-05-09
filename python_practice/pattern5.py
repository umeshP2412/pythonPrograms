
c = int(input("Give counter: "))
for i in range(c-1):
    for j in range(c-1,i,-1):
        print(" ",end="")
    for m in range(i):
        print("*",end="")
    print(end="\n")

for i in range(c):
    for j in range(i):
        print(" ",end="")
    for n in range(c-1,i,-1):
        print("*",end="")
    print(end="\n") 