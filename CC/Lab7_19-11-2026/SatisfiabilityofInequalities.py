import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])

    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    strict = []
    p = 2
    for _ in range(m):
        u = int(data[p])
        op = data[p + 1]
        v = int(data[p + 2])
        p += 3
        if op == b"=":
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[rv] = ru
        elif op == b"<":
            strict.append((u, v))
        else:
            strict.append((v, u))

    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for u, v in strict:
        ru, rv = find(u), find(v)
        if ru == rv:
            print("IMPOSSIBLE")
            return
        adj[ru].append(rv)
        indegree[rv] += 1

    roots = [i for i in range(1, n + 1) if find(i) == i]
    q = deque(r for r in roots if indegree[r] == 0)
    visited = 0

    while q:
        curr = q.popleft()
        visited += 1
        for nxt in adj[curr]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    print("POSSIBLE" if visited == len(roots) else "IMPOSSIBLE")

if __name__ == "__main__":
    main()
