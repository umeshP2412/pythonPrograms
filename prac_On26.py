import math 
import string

vals = [1,3,2,4,7]

print(vals)
vals.append(6)
vals.append(88)
print(vals)
vals.append(5)
vals.sort()
for i in vals:
    print(i)

a = "Helllo World"
typeA = type(a)
print(a.upper())
print(a.replace("World", "Hello"))
print(typeA)
print("type of typeA: ",type(typeA))
if typeA == "<class 'str'>":
    print("It is String")
else:
    print("It is Integer")

name = "Umesh"
name2 = "Sagar"
#print(("This is {} And he is good boy {}").format(name, name2))

l = len(name)
print(l)
print(range(l))
for i in range(l):
    print(i, end='')
    print(name[i])