def fibo(Num):
    t = 1
    for i in range(Num,0,-1):
        t = t*i
    return t
        

#fibo(5)

if __name__ == "__main__":
    n = int(input("Give number: "))
    print("Factorial of",n,"is:", fibo(n))