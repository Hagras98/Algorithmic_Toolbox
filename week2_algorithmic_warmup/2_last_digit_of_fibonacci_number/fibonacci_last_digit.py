# Uses python3
import sys

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
        
    minus1 = 1
    minus2  = 0

    for _ in range(n - 1):
        fib = (minus1 + minus2) % 10
        minus2 = minus1
        minus1 = fib
        
    return fib

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
