# Uses python3
import sys

def gcd(a, b):    
    if b == 0:
        return a   

    return gcd(min(a,b), max(a,b) % min(a,b))

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
