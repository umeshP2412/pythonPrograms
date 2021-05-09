def factors(num):
    l = []
    for i in range(1,num+1):
        if num%i == 0:
            l.append(str(i))
    m = ' '.join(l)
    return(str(m))


if __name__ == "__main__":
    n = int(input("Give number: "))
    print(factors(n))