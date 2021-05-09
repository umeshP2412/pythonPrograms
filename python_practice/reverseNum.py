h = int(input("Give number: "))
l = list(str(h))
print(l)
m=[]
for i in range(len(l)-1,-1,-1):
    m.append(l[i])
num = "".join(m)
print(int(num))

#Logically ///// ex. h 457
rev=0
while h>0:
    rem = h%10  #returns remainder 7 in first cycle, ... 2nd cyc ---> rem = 45%10 = 5
    rev = (rev*10)+rem #forming reverse 0 + 7 in first cycle rev=7, ....2nd cyc ----> rev = 70+5=75 
    h = h//10 # returns absolute value after divide 45,.... 2nd cyc ---> 45//10 = 4

print(rev)
