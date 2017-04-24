def factorial(n):
    if not n:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))
