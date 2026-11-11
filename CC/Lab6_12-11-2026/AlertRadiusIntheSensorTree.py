import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    target_value = int(data[0])
    k = int(data[1])
    n = int(data[2])
    root = int(data[3])

    value = [0] * n
    left = [0] * n
    right = [0] * n
    parent = [-1] * n
    target_idx = -1

    p = 4
    for i in range(n):
        v = int(data[p])
        l = int(data[p + 1])
        r = int(data[p + 2])
        value[i], left[i], right[i] = v, l, r
        if v == target_value:
            target_idx = i
        if l != -1:
            parent[l] = i
        if r != -1:
            parent[r] = i
        p += 3

    visited = [False] * n
    visited[target_idx] = True
    q = deque([(target_idx, 0)])
    res = []

    while q:
        curr, dist = q.popleft()
        if dist == k:
            res.append(value[curr])
        elif dist < k:
            for nxt in (left[curr], right[curr], parent[curr]):
                if nxt != -1 and not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, dist + 1))

    if not res:
        print("NONE")
    else:
        res.sort()
        print(" ".join(map(str, res)))

if __name__ == "__main__":
    main()
