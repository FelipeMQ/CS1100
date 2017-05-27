def bubblesort(list):
    for p in range(len(list)-1,0,-1):
        for i in range(p):
            if list[i]<list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
    return list

def juegovida(mat,t):
    cnts = []
    container = []

    for cnt in range(len(mat)+2):
        container.append([])
        for ind in range(len(mat[cnt-2])+2):
            container[cnt].append(0)

    for cnt in range(1, len(mat)+1):
        for ind in range(1, len(mat) + 1):
            container[cnt][ind] = mat[cnt-1][ind-1]

    out = [i[:] for i in container]

    for z in range(t): #t iteraciones
        cnts.append(0)
        for x in range(1, len(container)-1):
            for y in range(1, len(container[x])-1):
                #print(x,y,vecinos(container,x,y))
                if vecinos(container,x,y) == 3:
                    if container[x][y]==0: #validar que sea nacimiento
                        cnts[z] += 1
                    out[x][y] = 1 #nacer
                elif vecinos(container,x,y) < 2:
                    out[x][y] = 0 #morir soledad
                elif vecinos(container,x,y) > 3:
                    out[x][y] = 0 #morir sobrepoblación
        container = [i[:] for i in out]
    return out,cnts

def columna(mat, ri, rf, j):
    return [row[j] for row in mat[ri:rf+1]]

def vecinos(matriz,i,j):
    return sum(columna(matriz,i-1,i+1,j-1) + columna(matriz,i-1,i+1,j) + columna(matriz,i-1,i+1,j+1)) - matriz[i][j]

#input
n,m,t = [int(x) for x in input().split(" ")]
if n>20 or m > 20 or t > 1000:
    print("Valor incorrecto")
else:
    mat=[]
    for j in range(n):
        mat.append([])
    for i in range(n):
        mat[i] = [int(y) for y in input().split(" ")]
    #proceso
    rmat,cnts = juegovida(mat,t)
    #resultados
    print(rmat)
    print("\n".join([" ".join([str(x) for idx,x in enumerate(row) if idx not in [0,len(row)-1]]) for ind,row in enumerate(rmat) if ind not in [0, len(rmat)-1]]))
    print("\n".join([str(cnt) for cnt in bubblesort(cnts)]))