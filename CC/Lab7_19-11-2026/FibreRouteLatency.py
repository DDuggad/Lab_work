import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])

    adj = [[] for _ in range(n + 1)]
    p = 2
    for _ in range(m):
        u = int(data[p])
        v = int(data[p + 1])
        w = int(data[p + 2])
        adj[u].append((v, w))
        adj[v].append((u, w))
        p += 3

    INF = 10**18
    dist = [INF] * (n + 1)
    dist[1] = 0
    heap = [(0, 1)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    out = [str(dist[i] if dist[i] < INF else -1) for i in range(1, n + 1)]
    print(" ".join(out))

if __name__ == "__main__":
    main()
