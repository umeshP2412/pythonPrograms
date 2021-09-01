str = "geeksforgeeks is for geeks"
str2 = "geeks"
 
# using find() to find first occurrence of str2
# returns 8
print ("The first occurrence of str2 is at : ", end="")
print (str.find( str2, 4) ) #find(string, start, end)
 
# using rfind() to find last occurrence of str2
# returns 21
print ("The last occurrence of str2 is at : ", end="")
print ( str.rfind( str2, 4) )   #rfind(string, start, end)

if str.startswith(str2):
    print("str starts with 'geeks'")
elif str.endswith(str2):
    print("str ends with 'geeks'")
else:
    print("string doesn't match")

string1 = "UMESH PATIL"
if string1.isupper():
    print("string1 is in upper case..")
string2 = "umesh patil"
if string2.islower():
    print("string2 is lower case..")