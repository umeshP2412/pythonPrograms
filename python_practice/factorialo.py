n = int(input("Value: ")) 
l = []
for i in range(1,n+1):
    l.append(i)
m=1
for j in l:
    m = j*m

print(m)

n = [int(h) for h in str(m)]
print(n)
n.reverse()
print(n)
c=0
for k in n:
    p = int(k)
    if p != 0:
        break
    else:
        c =c+1

print(c)


