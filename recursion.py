def fctorial(n):
    # base cond 
    if n == 0:
        return 1
    else:
        return n * fctorial(n-1)
print(fctorial(5))
def fibo(n):
    # base cond 
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(5))