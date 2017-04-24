def tresn(nx, i):
    i = i + 1
    if nx == 1:
        return i
    elif nx % 2 == 1:
        return tresn(3 * nx + 1, i)
    else:
        return tresn(nx / 2, i)

n, m = input().split(" ")
n, m = int(n), int(m)
if (n in range(1,1000000) and m in range(1,1000000)):
    M = 0
    for i in range(n,m+1):
        tresn(i, 0)
        if M < tresn(i, 0):
            M = tresn(i, 0)
    print(n, m, M)