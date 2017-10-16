frase = input().lower()
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
contador = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for letra in frase:
    i=0
    for car in alfabeto:
        if letra == car:
            contador[i]=contador[i]+1
        i=i+1
i=0
while i<26:
    if contador[i]>0:
        print(alfabeto[i],": ",contador[i])
    i=i+1
