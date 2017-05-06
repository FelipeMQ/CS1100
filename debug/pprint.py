from inspect import getmembers
from pprint import pprint
a,b=input().split(" ")

a=int(a)
b=int(b)

q=4-a
w=6-b
if a<0 or b<0 or a>=4 or a>=6:
    print("Valor incorrecto")
else:
    print("+{},+{}".format(q,w))

#pprint(globals())
#pprint(locals())
pprint(getmembers("Valor incorrecto"))


