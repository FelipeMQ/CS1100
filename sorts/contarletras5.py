lineas = []
alps = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
cnts = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while True:
    val = input().lower()
    if val=="fin":
        break
    lineas += [val]

if len(lineas) == 0:
    print("Valor incorrecto")
else:
    for lin in lineas:
        for ind, car in enumerate(lin):
            ialp = alps.count(car)
            if ialp>0:
                cnts[alps.index(car)]+=1

    for i in range(len(alps)-1,-1,-1):
        if cnts[i] == 0:
            del cnts[i]
            del alps[i]

    for j,y in enumerate(alps):
        print(alps[j],":",cnts[j],sep="")