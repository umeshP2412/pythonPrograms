def isPerfect(num):
    v = 0
    for i in range(1,num):
        if num%i == 0:
            v = v+i
   
    if v == num:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input("Give n:"))
    if isPerfect(n):
        print("Given number is Perfect..")
    else:
        print("Given Number is not perfect ***")