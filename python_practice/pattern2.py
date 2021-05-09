ch = int(input("Give counter: "))
for i in range(ch,0,-1):
    for j in range(i,0,-1):
        print("*",end="")
    print(end="\n")
