m = []
S="Geeks"
S = list(S)
print(S)
print(len(S))
for i in range(len(S)):
    if i%2 == 0:
        #print(type(S))
        print(S[i])
        m.append(S[i])

m = ''.join(m)
print(m)
        