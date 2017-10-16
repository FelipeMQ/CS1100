frase = input()
letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','Y','X','Z','¿','?','-','0','1','2','3','4','5','6','7','8','9','¡','!']
_colum = [0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5,0,1,2,3,4,5]
_filas = [0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6]
if frase == frase.upper():
    for c in range(len(frase)):
        if (frase[c] in letras and (not frase[c]==' ')):
            posicion = letras.index(frase[c])
            print(_filas[posicion], _colum[posicion])
else:
    print("Valor incorrecto")
