n = int(input())
let = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
if n == 0 or n > 27:
    print("Valor incorrecto")
else:
    def triangle(n):
        k = 2 * n - 2
        for i in range(0, n):
            for j in range(n-1, k):
                print(end=" ")
            k = k - 1
            num = 65
            for j in range(0, i + 1):
                ch = let[j]
                print(ch, end=" ")
                num = num + 1
            print("\r")
    triangle(n)