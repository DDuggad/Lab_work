import heapq

def h_misplaced(s, goal):
    return sum(1 for i in range(9) if s[i] != 0 and s[i] != goal[i])

def h_manhattan(s, goal):
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

def a_star(initial, goal, mode):
    h_func = h_misplaced if mode == 1 else h_manhattan
    pq = [(h_func(initial, goal), 0, initial)]
    visited = set()
    while pq:
        f, g, cur = heapq.heappop(pq)
        if cur in visited:
            continue
        visited.add(cur)
        if cur == goal:
            return g, len(visited)
        for nxt in get_neighbors(cur):
            if nxt not in visited:
                heapq.heappush(pq, (g + 1 + h_func(nxt, goal), g + 1, nxt))
    return -1, len(visited)

initial = tuple(map(int, input("Enter initial state (9 values, 0 for blank): ").split()))
goal = tuple(map(int, input("Enter goal state (9 values, 0 for blank): ").split()))

cost1, vis1 = a_star(initial, goal, 1)
cost2, vis2 = a_star(initial, goal, 2)

print(f"\nA* (Misplaced Tiles)    -> Cost: {cost1}, States Explored: {vis1}")
print(f"A* (Manhattan Distance) -> Cost: {cost2}, States Explored: {vis2}")
