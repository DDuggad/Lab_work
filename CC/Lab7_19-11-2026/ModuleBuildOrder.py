import sys
import heapq

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])

    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    p = 2
    for _ in range(m):
        a = int(data[p])
        b = int(data[p + 1])
        adj[a].append(b)
        indegree[b] += 1
        p += 2

    heap = [i for i in range(1, n + 1) if indegree[i] == 0]
    heapq.heapify(heap)
    order = []

    while heap:
        u = heapq.heappop(heap)
        order.append(str(u))
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(heap, v)

    if len(order) < n:
        print("CYCLE")
    else:
        print(" ".join(order))

if __name__ == "__main__":
    main()
