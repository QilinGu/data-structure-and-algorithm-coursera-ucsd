# Uses python3
import sys

def gcd_naive(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    if a>b:
        print(gcd_naive(a, b))
    else:
        print(gcd_naive(b, a))
