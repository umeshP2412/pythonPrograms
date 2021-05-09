def hcf(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    v = []
    for i in range(1,small):
        if num1%i == 0 and num2%i == 0:
            v.append(i)

    return max(v)

def lcm(num1, num2):
    return (num1*num2)/hcf(num1, num2)

if __name__ == "__main__":
    num1 = int(input("Give num1: "))
    num2 = int(input("Give num2: "))
    print("HCF: ",hcf(num1, num2))
    print("LCM: ",lcm(num1, num2))