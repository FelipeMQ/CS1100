Letras=["a","b","c","d","e","f","g","h"]
Numeros=[1,2,3,4,5,6,7,8]
Colores=["b","n"]
Fichas=["p","t","c","a","r-","r+"]

for n in Numeros:
    for l in Letras:
        for c in Colores:
            for f in Fichas:
                print(f, c, n, l)