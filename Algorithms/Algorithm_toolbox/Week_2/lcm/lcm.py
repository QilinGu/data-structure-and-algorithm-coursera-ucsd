# Uses python3
import sys

def lcm_naive(a, b):
    ucln = 1
    if a> b:
        ucln = gcd_naive(a, b)
    else:
        ucln = gcd_naive(b, a)
    return int(int(a/ucln)*b)

def gcd_naive(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
        
if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

