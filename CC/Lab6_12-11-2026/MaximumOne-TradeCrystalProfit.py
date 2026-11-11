import sys

def max_profit(values):
    min_val = float('inf')
    max_p = 0
    for v in values:
        if v < min_val:
            min_val = v
        if v - min_val > max_p:
            max_p = v - min_val
    return max_p

data = list(map(int, sys.stdin.read().split()))
if data:
    n = data[0]
    values = data[1:1+n]
    print(max_profit(values))
