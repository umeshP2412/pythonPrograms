def print_formatted(number):

    width = len("{:b}".format(number))
    print(width,"{:b}".format(number))
    for i in range(1,number+1):
        #string formatting using format() function
        print("{0:{width}d}".format(i,width=6),end=" ")
        #below makes number octal with spacing given by width
        print("{0:{width}o}".format(i,width=6), end=" ")
        print("{0:{width}X}".format(i,width=6), end=" ")
        print("{0:{width}b}".format(i,width=6))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)