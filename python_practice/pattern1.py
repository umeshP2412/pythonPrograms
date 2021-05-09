''' pattern is:
*
**
***
****
'''
i = int(input("Give value of i: "))
for i in range(i):
    for j in range(i+1):
        print("*", end="")
    print(end="\n")

