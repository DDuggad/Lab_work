import math

def alphabeta(d, idx, is_max, alpha, beta):
    if d == max_d:
        visited.append(leaves[idx])
        return leaves[idx]
    if is_max:
        val = -math.inf
        for i in range(b):
            val = max(val, alphabeta(d + 1, idx * b + i, False, alpha, beta))
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return val
    else:
        val = math.inf
        for i in range(b):
            val = min(val, alphabeta(d + 1, idx * b + i, True, alpha, beta))
            beta = min(beta, val)
            if beta <= alpha:
                break
        return val

max_d = int(input("Enter depth of tree: "))
b = int(input("Enter branching factor: "))
leaves = list(map(int, input(f"Enter {b**max_d} leaf values: ").split()))
visited = []

ans = alphabeta(0, 0, True, -math.inf, math.inf)
print("Optimal Root Value:", ans)
print("Evaluated Leaves:", visited)
