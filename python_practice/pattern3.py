'''
*
**
***
****
*****
****
***
**
*
'''
a = int(input("Give counter: "))
for i in range(0,a):
    for j in range(0,i):
        print("*",end="")
    print(end="\n")
for k in range(a,0,-1):
    for l in range(k,0,-1):
        print("*",end="")
    print(end="\n")

for i in range(0,a):
    print(i,end="")

print(end="\n")
for k in range(a,0,-1):
    print(k,end="")