'''
def sum(a, *b):
    c = a
    for i in b:
        c = c+i
    print(c)

sum(5, 3, 1, 5)
'''
'''
def person(name, age=18):
    print(name)
    print(age-3)

name="Umesh"

person("Sagar", 23)
'''
'''
def person(name, **data):
    print(data.keys())
    print(data.values())
    for i,j in data.items():
        print(i,"-", j)

person("Umesh", age="26", gender="male", city="Ahmedabad", mob="9558829646")
'''

def count(lst):
    even=0
    odd=0
    zero=0
    for i in lst:
        if i == 0:
            zero += 1
        elif i%2 ==0:
            even += 1
        else:
            odd+=1
    return even, odd, zero

lst=[21, 34, 0, 12, 13, 45, 67, 32, 44, 31, 0]
even, odd, zero = count(lst)
print('even =',even,'odd =', odd)
print('even: {} odd: {}'.format(even, odd))
if zero != 0:
    print(zero, "zero detected")
