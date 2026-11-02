import heapq

initial = (2, 8, 3, 1, 6, 4, 7, 0, 5)
goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)

def h_misplaced(s):
    return sum(1 for i in range(9) if s[i] != 0 and s[i] != goal[i])

def h_manhattan(s):
    d = 0
    for i in range(9):
        if s[i] != 0:
            gi = goal.index(s[i])
            d += abs(i // 3 - gi // 3) + abs(i % 3 - gi % 3)
    return d

def get_neighbors(s):
    idx = s.index(0)
    r, c = idx // 3, idx % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    res = []
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nidx = nr * 3 + nc
            lst = list(s)
            lst[idx], lst[nidx] = lst[nidx], lst[idx]
            res.append(tuple(lst))
    return res

def a_star(mode="misplaced"):
    h_func = h_misplaced if mode == "misplaced" else h_manhattan
    pq = [(h_func(initial), 0, initial, [])]
    visited = set()
    while pq:
        f, g, cur, path = heapq.heappop(pq)
        if cur in visited:
            continue
        visited.add(cur)
        if cur == goal:
            return g, len(visited)
        for nxt in get_neighbors(cur):
            if nxt not in visited:
                heapq.heappush(pq, (g + 1 + h_func(nxt), g + 1, nxt, path + [nxt]))

cost1, visited1 = a_star("misplaced")
cost2, visited2 = a_star("manhattan")

print(f"A* (Misplaced Tiles)    -> Cost: {cost1}, States Explored: {visited1}")
print(f"A* (Manhattan Distance) -> Cost: {cost2}, States Explored: {visited2}")
