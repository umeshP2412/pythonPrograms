str = "ThisIsaString"
#print(str[0:4])
print(str[slice(1, 4)])

print(str[0:3]+str[5:len(str)])

str2 = "This is 2nd String"
print(str2[0])

for i in range(len(str2)+1):
    print(str2[0:i])

