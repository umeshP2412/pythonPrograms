a = input("Give a string: ")
print(a)
a.split()
print(a.split())
print(a.split(":")) 
'''for i in a.split():
    print(i)'''

b = input("Give continues string: ")
for i in range(0,len(b),3):
    print(i)
    print(b[i:i+3])
    