import re

lista1 = [3,4,52,3,8, 3,53,1]
lista2 = [5,33,56,77,43,1,4,3]
lista3 = lista1 + lista2
print(set([x for x in lista3 if lista3.count(x)>1]))

lista1 = [3,4,52,3,8,3,53,8,1]
print([x for x in lista1 if lista1.count(x)>1])

lista = []
for x in re.finditer(r"(\d+)(,)*(\d+)*(,)*(\1)",",".join([str(x) for x in lista1])):
    print(x.group())