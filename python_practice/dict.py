thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#change value
thisdict["year"]=2020
print(thisdict)

#update value
thisdict.update({"year":1998})
print(thisdict)

# adding value
#thisdict["color"]="red"
thisdict.update({"Color":"Red"})
print(f"added {thisdict}")

#remove item
thisdict.pop("Color")
print(f"removed color {thisdict}")

#loop
#print all keys
for i in thisdict:
    print(i)

#print all values
for i in thisdict:
    print(thisdict[i])

#print both
for i in thisdict:
    print(i, ':', thisdict[i] )

for i,j in thisdict.items():
    print(i,j)

#copy dictionary
thatdict = dict(thisdict)
print(thatdict)