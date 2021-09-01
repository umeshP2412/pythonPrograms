def hcf(l):
    li=[]
    for k in l:
        li.append(int(k)) #convert that splitted O/P to integer
    #print(li)
    s = min(li)

    str1=""
    lent = len(li)
    #print(lent)

    #make string for checking condn
    for num in li:
        str1 = str1+str(num)+"%i == 0 "
        lent=lent-1
        if lent != 0:
            str1 = str1+"and "
    
    #for 18 12 13 24 26 input
    #18%i == 0 and 12%i == 0 and 13%i == 0 and 24%i == 0 and 26%i == 0
    #print(str1)
    facto=[]
    #replace i with integer:
    for i in range(1,s):
        if eval(str1):
            facto.append(i)


    return max(facto)

def lcm(l):
    mul = 1
    for k in l:
        mul = mul*int(k)
    
    return int(mul/hcf(l))

if __name__ == "__main__":
    k = input("Give value for LCM, HCF:") #take input as string
    l = []
    l = k.split() #split input by space using split() function
    #print(l)
    print("hcf: ",hcf(l))
    print("lcm: ",lcm(l))
