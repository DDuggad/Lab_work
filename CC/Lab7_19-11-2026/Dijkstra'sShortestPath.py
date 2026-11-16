import sys
import heapq

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])

    adj = [[] for _ in range(n)]
    p = 2
    for _ in range(m):
        u = int(data[p])
        v = int(data[p + 1])
        w = int(data[p + 2])
        adj[u].append((v, w))
        p += 3

    INF = 10**18
    dist = [INF] * n
    dist[0] = 0
    pq = [(0, 0)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    ans = [str(d if d < INF else -1) for d in dist]
    print(" ".join(ans))

if __name__ == "__main__":
    solve()
