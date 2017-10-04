
def mover(mapa, xi, yi, vector):
    for celda in range(n*n):
        for paso in vector:
            tx = xi + mx[paso]
            ty = yi + my[paso]
            if (tx >= 0 and tx < n and ty >= 0 and ty < n and mapa[tx][ty] == 0):
                mapa[tx][ty] = mapa[xi][yi] + 1
                xi = tx
                yi = ty
                break

if __name__ == "__main__":
    n = int(input().strip())

    if (n>=2 and n<=60):
        d = input().strip()
        mx = [0, 0, -1, 1]
        my = [1, -1, 0, 0]
        mapa = [[0 for i in range(n)] for j in range(n)]
        x, y = [int(corde) for corde in input().split(' ')]
        mapa[x][y] = 1

        if (d=='e'):
            mover(mapa,x,y,[0,2,3,1])
        if (d=='o'):
            mover(mapa,x,y,[1,2,3,0])
        if (d=='n'):
            mover(mapa,x,y,[2,0,1,3])
        if (d=='s'):
            mover(mapa,x,y,[3,0,1,2])

        for x in range(n):
            for y in range(n):
                print(mapa[x][y], end="")
                if (y!=n-1):
                    print(" ", end="")
            print()