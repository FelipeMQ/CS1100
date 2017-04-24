x=input()

(a,b)=x

q=4-a
w=6-b
if a<0 or b<0 or a>=4 or a>=6:
    print("Valor incorrecto")
else:
    print("+{},+{}".format(q,w))