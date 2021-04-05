#Swapping without 3rd variable
a = int(input("Give value a: "))
b = int(input("Give value b: "))
print(f"value of a={a}")
print(f"value of b={b}")
a=a+b
b=a-b
a=a-b
#a =3
#b =4
#a=7 after a= a+b
"""b=3  after b= a-b
a=4  after a=a-b 
print(f"value of a={a}")
print(f"value of b={b}")
"""
print(f"value of a={a}")
print(f"value of b={b}")
