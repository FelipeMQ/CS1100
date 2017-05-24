def bubblesort(list,lcnt):
    for p in range(len(list) - 1, 0, -1):
        for i in range(p):
            if list[i] > list[i + 1]:
                list[i],list[i + 1] = list[i + 1],list[i]
                lcnt[i], lcnt[i + 1] = lcnt[i + 1], lcnt[i]
    return list,lcnt

lineas = []
alpha = "0123456789abcdefghijklmnopqrstuvwxyz"
alps = []
cnts = []
while True:
    val = input().lower()
    if val == "fin":
        break
    lineas += [val]

if len(lineas) == 0:
    print("Valor incorrecto")
else:
    for lin in lineas:
        for ind, car in enumerate(lin):
            ialp = alpha.count(car)
            if ialp > 0:
                if car not in alps:
                    alps.append(car)
                    cnts.append(1)
                else:
                    indcar = alps.index(car)
                    cnts[indcar] += 1

    alps,cnts = bubblesort(alps,cnts)

    for j, y in enumerate(alps):
        print(alps[j], ":", cnts[j], sep="")