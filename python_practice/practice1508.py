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

