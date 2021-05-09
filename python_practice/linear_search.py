
def search(list,n):
    p=1
    for i in list:
        p = p+1
        if i == n:
            return True
    return False, p
a=[]

while True:
    l = input("")
    if l == "":
        break
    else:
        a.append(int(l))  

print(a)

n = int(input("Value to be found: "))

print(search(a,n)[1])

if search(a,n):
    print("Found")
else:    
    print("Not Found")