import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    LOG = 18
    up = [[0] * n for _ in range(LOG)]
    depth = [0] * n
    visited = [False] * n

    bfs_queue = [0]
    visited[0] = True

    head = 0
    while head < len(bfs_queue):
        u = bfs_queue[head]
        head += 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                up[0][v] = u
                bfs_queue.append(v)

    up[0][0] = 0
    for k in range(1, LOG):
        for i in range(n):
            up[k][i] = up[k - 1][up[k - 1][i]]

    results = []
    for _ in range(q):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2

        if depth[u] < depth[v]:
            u, v = v, u

        for k in range(LOG - 1, -1, -1):
            if depth[u] - (1 << k) >= depth[v]:
                u = up[k][u]

        if u == v:
            results.append(str(u))
            continue

        for k in range(LOG - 1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]

        results.append(str(up[0][u]))

    print("\n".join(results))

if __name__ == "__main__":
    main()
