#Swapping without 3rd variable
a = int(input("Give value a: "))
b = int(input("Give value b: "))
print(f"value of a={a}")
print(f"value of b={b}")
#a =3
#b =4
#a=7 after a= a+b
a=a+b   #3+4    a=7
b=a-b   #(3+4)-4    b=3
a=a-b   #(3+4)-3    a=4

"""b=3  after b= a-b
a=4  after a=a-b 
print(f"value of a={a}")
print(f"value of b={b}")
"""
print(f"value of a={a}")
print(f"value of b={b}")
