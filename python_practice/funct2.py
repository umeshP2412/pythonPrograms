a = int(input("Give a: "))
b = int(input("Give b: "))
def smartdiv(a,b):
    if a>b:
        print(float(a)/float(b))
    else:
        print(float(b)/float(a))

smartdiv(a,b) 