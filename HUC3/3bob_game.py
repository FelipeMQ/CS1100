#!/bin/python3
import pprint
import sys

def posible(mat,x,y):
    if x-1>=0 and y>=0 and mat[x-1][y]!='X':
        return True

def mover(mat,x,y,paso,jugador):
    if x+paso[0]==0 and y+paso[1]==0:
        if jugador == 'B':
            return 1
        else:
            return 0

    if mover(x-1,y) < mover(x-1,y-1) and mover(x,y-1) < mover(x-1,y-1):
            return mover(x-1,y-1)

def arbol(ind,mat):
    dict.update({ind:mat})

if __name__ == "__main__":
    q = int(input().strip())
    dict = {}
    for a0 in range(q):
        n = int(input().strip())
        board = []
        board_i = 0
        i = 0
        for board_i in range(n):
            board_t = str(input().strip().split())
            board.append([])
            for x in board_t:
                if (x=='.'):
                    board[board_i].append(0)
                if x == 'K':
                    i = i + 1
                    board[board_i].append(i)
                if x == 'X':
                    board[board_i].append(-1)

        for x in range(n):
            for y in range(n):
                if (board[x][y]!=0):
                    arbol(board[x][y], [x,y])
