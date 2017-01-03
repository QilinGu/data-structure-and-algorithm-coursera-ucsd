#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    a_plus = sorted([i for i in a if i>= 0])
    #print(a_plus)
    n_a_plus = len(a_plus)
    a_minus = sorted([-i for i in a if i< 0])
    #print(a_minus)
    n_a_minus = len(a_minus)
    b_plus = sorted([i for i in b if i>= 0])
    #print(b_plus)
    n_b_plus = len(b_plus)
    b_minus = sorted([-i for i in b if i< 0])
    #print(b_minus)
    n_b_minus = len(b_minus)
    res = 0
    if n_a_plus >= n_b_plus:
        for i in range(n_b_plus):
            res += b_plus[n_b_plus-1-i] * a_plus[n_a_plus-1-i]
            #print(i,b_plus[n_b_plus-1-i],a_plus[n_a_plus-1-i])
        for i in range(n_a_minus):
            res += b_minus[n_b_minus-1-i] * a_minus[n_a_minus-1-i]
            #print(i, b_minus[n_b_minus-1-i], a_minus[n_a_minus-1-i])
        #print(n_a_plus - n_b_plus)
        for i in range(n_a_plus - n_b_plus):
            res -= a_plus[n_a_plus - n_b_plus-1-i]*b_minus[i]
            #print(i, a_plus[n_a_plus - n_b_plus-1-i], b_minus[i])
    else:
        for i in range(n_a_plus):
            res += a_plus[n_a_plus-1-i] * b_plus[n_b_plus-1-i]
        for i in range(n_b_minus):
            res += a_minus[n_a_minus-1-i] * b_minus[n_b_minus-1-i]
        for i in range (n_b_plus - n_a_plus):
            res -= b_plus[n_b_plus - n_a_plus-1-i]*a_minus[i]
    return res
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data = list(map(int, input().split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
