# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    n = n%get_pisano(m)
    if n <= 1:
        return n
    
    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%m
    if current == 0:
        return m-1
    return current 
def get_pisano(n):
    c=[1,1]
    a=[]
    while(c in a)<1%n:
        a+=[c]
        c=[c[1],sum(c)%n]
    module = (len(a) or 1)
    return (module)
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))

