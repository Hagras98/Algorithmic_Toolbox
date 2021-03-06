# Uses python3
import sys
def calc_fib(n):   
    
    if n <= 1:
        return n
    minus1 = 1
    minus2 = 0
    for i in range(n-1):
        fib = minus1 + minus2
        minus2 = minus1
        minus1 = fib
        
    return fib

def fibonacci_partial_sum(from_, to):
    
    fibs = [0, 1]
    i = 2
    while(True):
        fibs.append(calc_fib(i) % 10)
        if fibs[i] == 1 and fibs[i-1] == 0:
            break
        i += 1
    period = len(fibs) - 2
    
    upper = 0
    for num in fibs[: (to % period) + 1]:        
        upper += num   
    
    lower = 0
    if(from_ > 0):  
        for num in fibs[: ((from_ - 1) % period) + 1]:
            lower += num
    
    if lower > upper:
        upper+=10
    
    return (upper-lower) % 10

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
