# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:28:24 2019

@author: LENOVO
"""
'''
movies = ['The great Grail',"The life", "Wow"]
movies.append("KGF")
movies.append("7500")
print(movies)

movies.extend(["KGF"])
#movies.pop()
movies.pop(2)
print(movies)
'''
'''
k=0
for i in movies:
    k+=1
    print(i, end=' ')
'''
'''
count=0
while count < len(movies):
    print(movies[count])
    count += 1
'''
'''
movies.append(["RDJ", "steve rogers", "Sacrlett", "Mark Ruffalo"])
print(movies)

for i in movies:
    if isinstance(i, list):
        print(i)
        
print(movies.count("KGF"))
#print(movies.pop())

print(id(movies))
'''
#concept key:value OR dictionary<-mapping

mobile = {'Umesh':'Realmi', 'Parth':'Iphone', 'Yash':'Mi'}
print(mobile['Umesh'])
print(mobile.get('Parth'))
mobile.update({"Sagar":"Mi"})
print(mobile)
print(mobile.keys())
print(list(mobile.keys()))


#Update list

mobile['Parth']= 'Vivo'
print(mobile)
