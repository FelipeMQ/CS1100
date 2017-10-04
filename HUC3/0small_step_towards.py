#!/bin/python3

import sys

def solve(opr):
    # Complete this function
    if "0123456789".count(opr[0])==0:
        return 0
    if opr[1]=='+':
        return int(opr[0])+int(opr[2])
    if opr[1]=='-':
        return int(opr[0])-int(opr[2])

if __name__ == "__main__":
    opr = input().strip()
    result = solve(opr)
    print(result)