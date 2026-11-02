import math
import random

def cost(s):
    c = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if s[i] == s[j] or abs(s[i] - s[j]) == abs(i - j):
                c += 1
    return c

def simulated_annealing():
    random.seed(42)
    cur = [random.randint(0, 7) for _ in range(8)]
    T = 100.0
    alpha = 0.95
    while T > 0.001 and cost(cur) > 0:
        nxt = list(cur)
        col = random.randint(0, 7)
        nxt[col] = random.randint(0, 7)
        delta_E = cost(cur) - cost(nxt)
        if delta_E > 0:
            cur = nxt
        else:
            if random.random() < math.exp(delta_E / T):
                cur = nxt
        T *= alpha
    return cur

sol = simulated_annealing()
print("Final 8-Queens Board:", sol)
print("Attacking Pairs (Cost):", cost(sol))
