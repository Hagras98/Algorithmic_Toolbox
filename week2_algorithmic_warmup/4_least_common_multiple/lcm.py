# Uses python3
import sys

def gcd(a, b):    
    if b == 0:
        return a

    return gcd(min(a,b), max(a,b) % min(a,b))

def lcm(a, b):
    Lcm = 1
    
    while True:
        Gcd = gcd(a//Lcm, b//Lcm)
        Lcm *= Gcd
        
        if Gcd == 1:
            break
            
    return a*b//Lcm

if __name__ == '__main__':    
    a, b = map(int, input().split())
    print(lcm(a, b))

