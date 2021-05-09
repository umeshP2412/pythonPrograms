try:
    a = int(input("Give value of a: "))
except:
    print("Please Give a number...")
b = int(input("Give value of b: "))
choice = input("Give your inpt as, '+' '-' '*' '/' :")
if choice == "+":
    print(f"addition is: {a+b}")
elif choice == "-":
    print(f"subtraction is : {a-b}")
elif choice == "*":
    print(f"Multiplcation is : {a*b}")
elif choice == "/":
    print(f"Divide is : {a/b}")
else:
    print("Wrong Input")


