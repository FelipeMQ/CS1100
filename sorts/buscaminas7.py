def bubblesort(list):
    for p in range(len(list)-1,0,-1):
        for i in range(p):
            if list[i]<list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
    return list

def buscaminas(mat):
    bmbs = []
    cnts = []
    container = []

    for cnt in range(len(mat)+2):
        container.append([])
        cnts.append([])
        for ind in range(len(mat[cnt-2])+2):
            container[cnt].append(0)
            cnts[cnt].append(0)

    for cnt in range(1, len(mat)+1):
        for ind in range(1, len(mat[cnt-1]) + 1):
            container[cnt][ind] = mat[cnt-1][ind-1]
            if mat[cnt-1][ind-1]==ASTERISCO:
                cnts[cnt][ind] = 1
            else:
                cnts[cnt][ind] = 0

    out = [i[:] for i in container]

    for x in range(1, len(mat)+1):
        for y in range(1, len(mat[x-1])+1):
            if container[x][y] == ASTERISCO:
                out[x][y] = container[x][y]
            else:
                out[x][y] = bombas(cnts,x,y)
                if out[x][y] not in bmbs:
                    bmbs.append(out[x][y])
    return out,bmbs

def columna(mat, ri, rf, j):
    return [row[j] for row in mat[ri:rf+1]]

def bombas(matriz,i,j):
    return sum(columna(matriz,i-1,i+1,j-1) + columna(matriz,i-1,i+1,j) + columna(matriz,i-1,i+1,j+1)) - matriz[i][j]

#input
ASTERISCO = chr(42)
ESPACIO = chr(32)
ERROR_MESSAGE = ["Valor incorrecto"]
n,m = [int(x) for x in input().split(ESPACIO)]
if n>30 or m > 30:
    print(ERROR_MESSAGE[0])
else:
    boolast = 0
    mat,rmat,cnts = [],[],[]
    for j in range(n):
        mat.append([])
    for i in range(n):
        mat[i] = [row for row in list(input())]
        if ASTERISCO in mat[i]:
            boolast += 1
    if boolast>0:
        #proceso
        rmat,cnts = buscaminas(mat)
        #resultados
        print("\n".join(["".join([str(x) for idx,x in enumerate(row) if idx not in [0,len(row)-1]]) for ind,row in enumerate(rmat) if ind not in [0, len(rmat)-1]]))
        print("\n".join([str(cnt) for cnt in bubblesort(cnts)]))
    else:
        print(ERROR_MESSAGE[0])