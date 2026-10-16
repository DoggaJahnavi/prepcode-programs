def fibo (n):
    if n<15:
        return 0
    return n+fibo(n-1)
print(fibo(25))