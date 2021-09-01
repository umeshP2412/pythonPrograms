'''
try:
    a = int(input("Give value of a: "))
    b = int(input("Give value of b: "))
    ch = input("Give choice with symbol: ")
except:
    print("Please give integer value...")


  

if (ch == '+'):
    print(f"addition is {a+b}")
elif (ch == '-'):
    if (a>b):
        print(f"difference is {a-b}")
    else:
        print(f"difference is {b-a}")
elif (ch == '/'):
    print(f"division is {a/b}") 
elif (ch == '*'):
    print(f"multiplication is {a*b}")
else:
    print("Wrong input of choice ...")
    '''
'''
try:
    a = int(input("Give value of a: "))
    b = int(input("Give value of b: "))
    ch = input("Give choice with symbol: ")
except:
    print("Please give integer value...")

def CalcSwitch(choice):
    Calcs = {
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': a/b
    }
    print(Calcs.get(choice,"Invalid Input"))

CalcSwitch(ch)
'''
'''
def Armstrong(num):
    tmp = num
    l = len(str(num))
    p = 0
    for i in range(l):
        num2 = num%10
        p = p + (num2**l)
        num = num//10
    if tmp == p:
        return True
    else:
        return False

if __name__ == "__main__":
    start = int(input("give starting number: "))
    end = int(input("give end number: "))
    for j in range(start, end+1):
        if Armstrong(j):
            print(f"{j} is a Armstrong")


'''
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict:
    print(i+"-->", end='') 
    print(thisdict[i]) 
print(thisdict["year"])

thisdict.update({"year": 2020})
print(thisdict["year"])

thisdict.update({"color":"white"}) #if not found will add new
print(thisdict)

thisdict.pop("color") #key expected
print(thisdict)

print(thisdict.items())

for i,j in thisdict.items():
    print(i,j)

thisdict.keys()

#copy dictionary
thatdict = dict(thisdict)
print(thatdict)
'''
'''def factors(num):
    l = []
    for i in range(1,num+1):
        if num%i == 0:
            l.append(str(i))
    m = ' '.join(l)
    return(str(m))


if __name__ == "__main__":
    n = int(input("Give number: "))
    print(factors(n))
'''
'''
def fibo(num):
    m = 1
    for i in range(1, num+1):
        m=m*i
    return m

if __name__ == "__main__":
    n = int(input("Give value of n:"))
    print(fibo(n))
'''
'''
def hcf(num1, num2):
    if num1<num2:
        s = num1
    else:
        s = num2
    l=[]
    for i in range(1,s):
        if num1%i == 0 and num2%i ==0:
            l.append(i)
    m=max(l)
    return m

def lcm(num1, num2):
    return int((num1*num2)/hcf(num1,num2))

print("hcf:",hcf(18,24))

print("lcm:",lcm(18,24))
'''
def hcf(l):
    li=[]
    for k in l:
        li.append(int(k)) #convert that splitted O/P to integer
    #print(li)
    s = min(li)

    str1=""
    lent = len(li)
    #print(lent)

    #make string for checking condn
    for num in li:
        str1 = str1+str(num)+"%i == 0 "
        lent=lent-1
        if lent != 0:
            str1 = str1+"and "
    
    #for 18 12 13 24 26 input
    #18%i == 0 and 12%i == 0 and 13%i == 0 and 24%i == 0 and 26%i == 0
    #print(str1)
    facto=[]
    #replace i with integer:
    for i in range(1,s):
        if eval(str1):
            facto.append(i)


    return max(facto)

def lcm(l):
    mul = 1
    for k in l:
        mul = mul*int(k)
    
    return int(mul/hcf(l))

if __name__ == "__main__":
    k = input("Give value for LCM, HCF:") #take input as string
    l = []
    l = k.split() #split input by space using split() function
    #print(l)
    print("hcf: ",hcf(l))
    print("lcm: ",lcm(l))
    


