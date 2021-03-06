# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
        
    minus1 = 1
    minus2 = 0
    
    for i in range(n-1):
        fib = minus1 + minus2
        minus2 = minus1
        minus1 = fib        
        
    return fib

n = int(input())
print(calc_fib(n))
