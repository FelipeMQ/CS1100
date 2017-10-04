x,y = [1,2,3,1,2,3,3],[4,3,3,4,3,4,3]
plain = zip(x,y)

suma = [a*b for a,b in zip(x,y)]

print(suma)

for x,y in plain:
    print(x,y)
