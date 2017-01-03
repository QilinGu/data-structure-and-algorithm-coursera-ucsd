# Uses python3
import sys

def optimal_summands(n):
    summands = []
    number = 1
    while number*(number+1)/2 <= n:
        number += 1
    #print(number)
    for i in range(1,number-1):
        summands.append(i)
    summands.append(int(n - (number-1)*(number-2)/2))
    #write your code here
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
