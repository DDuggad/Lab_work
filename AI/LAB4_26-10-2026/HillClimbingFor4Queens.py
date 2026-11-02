initial = [3, 1, 2, 0]

def cost(s):
    c = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j] or abs(s[i] - s[j]) == abs(i - j):
                c += 1
    return c

def hill_climbing(state):
    cur = list(state)
    n = len(cur)
    step = 0
    print(f"Step {step}: State = {cur}, Cost = {cost(cur)}")
    while True:
        best_state = None
        best_cost = cost(cur)
        for i in range(n):
            for j in range(i + 1, n):
                nxt = list(cur)
                nxt[i], nxt[j] = nxt[j], nxt[i]
                c = cost(nxt)
                if c < best_cost:
                    best_cost = c
                    best_state = nxt
                    break
            if best_state:
                break
        if not best_state or best_cost >= cost(cur):
            break
        cur = best_state
        step += 1
        print(f"Step {step}: State = {cur}, Cost = {cost(cur)}")
    return cur

final_state = hill_climbing(initial)
print(f"Result: {final_state} with Cost {cost(final_state)}")
