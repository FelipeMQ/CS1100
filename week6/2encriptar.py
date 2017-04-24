frase = input()

alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
cripto = ['#','$','%','&','/','(',')','=','?','.',',','!','°','|','¬','\\','^','~','*','+','-','_','<','>',':',';']
salida = []

for c in frase:
    if c == " ":
        salida.append(" ")
        continue
    if c in alfabeto:
        cnt=0
        ind=0
        for a in alfabeto:
            if a==c:
                ind = cnt
            cnt = cnt + 1
        salida.append(cripto[ind])
    else:
        print("Debe ingresar la frase en mayúsculas.")
        break
print("".join(salida))
