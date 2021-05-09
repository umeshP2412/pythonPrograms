a = int(input("Give a: "))
b = int(input("Give b: "))
inp = input("Give choice in arithmatic sign: ")
def myFun(lm):
    switcher = {
        '+' : (a+b),
        '-' : (a-b),
        '*' : (a*b),
        '/' : (a/b)
    }
    print(switcher.get(lm,"Invalid Input"))

myFun(inp)