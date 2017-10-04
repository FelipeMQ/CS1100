#!/bin/python3

import sys

def llenamat(mat, x, y, tamano, valor):
    if (tamano == 1):
        mat[x][y] = mat[x][y] + valor
        return mat
    else:
        for cnt in range(x,x+tamano):
            for ind in range(y,y+tamano):
                if (cnt>=0 and ind>=0) and (cnt<len(mat) and ind<len(mat)):
                    mat[cnt][ind] = mat[cnt][ind] + valor
        return llenamat(mat, x+1, y+1, tamano-2, valor)

if __name__ == "__main__":
    n = int(input().strip())
    m = int(input().strip())

    maximo = 0
    container = []

    container = [[0 for i in range(n)] for j in range(n)]

    for a in range(m):
        x, y, w = input().strip().split(' ')
        x, y, w = [int(x), int(y), int(w)]
        xi = x-w+1
        yi = y-w+1
        tam = 2*w-1
        container = llenamat(container, xi, yi, tam, 1)

    print(max(map(max,container)))
