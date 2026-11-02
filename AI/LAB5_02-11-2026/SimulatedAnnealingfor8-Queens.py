import math
import random

def cost(s):
    c = 0
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j] or abs(s[i] - s[j]) == abs(i - j):
                c += 1
    return c

def simulated_annealing(initial, t_init, alpha):
    cur = list(initial)
    n = len(cur)
    T = t_init
    random.seed(42)
    while T > 0.001 and cost(cur) > 0:
        nxt = list(cur)
        col = random.randint(0, n - 1)
        nxt[col] = random.randint(0, n - 1)
        delta_E = cost(cur) - cost(nxt)
        if delta_E > 0:
            cur = nxt
        else:
            if random.random() < math.exp(delta_E / T):
                cur = nxt
        T *= alpha
    return cur

initial = list(map(int, input("Enter initial state (8 values between 0-7): ").split()))
t_val = float(input("Enter initial temperature (e.g. 100): "))
cooling_rate = float(input("Enter cooling rate alpha (e.g. 0.95): "))

sol = simulated_annealing(initial, t_val, cooling_rate)
print(f"\nFinal Board Configuration: {sol}")
print(f"Attacking Pairs (Cost): {cost(sol)}")
