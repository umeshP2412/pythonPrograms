def isArmstrong(num):
    l = len(str(num))
    tmp = num
    p = 0
    for i in range(l):
        rem = num % 10
        p = p + (rem**l)
        num = num//10
    
    if tmp == p:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    start = int(input("Give start: "))
    end = int(input("Give end number: "))
    for i in range(start, end+1):
        if isArmstrong(i) == "Yes":
            print(f"{i} is Armstrong Number")
        else:
            print(f"{i} is not a Armstrong Number ***")