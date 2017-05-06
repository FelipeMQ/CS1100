def tresn(nx, memo):
    if nx in memo:
        return memo[nx]
    elif nx & 1:
        l = tresn((nx << 1) + nx + 1, memo)
    else:
        l = tresn(nx >> 1, memo)
    memo[nx]=l+1
    return memo[nx]

def main():
    memo = {1: 1}
    while True:
        try:
            n, m = [int(a) for a in input().split()]
        except EOFError:
            break
        except ValueError:
            break
        if m<n:
            min = m
            max = n
        else:
            min = n
            max = m
        M = 0
        for i in range(min, max + 1):
            if M < tresn(i, memo):
                M = tresn(i, memo)
        print(n, m, M)

if __name__ == '__main__':
    main()