import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])

    edges = []
    p = 2
    for _ in range(m):
        u = int(data[p])
        v = int(data[p + 1])
        w = int(data[p + 2])
        edges.append((w, u, v))
        p += 3

    edges.sort()
    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total_weight = 0
    edge_count = 0

    for w, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            if size[ru] < size[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            size[ru] += size[rv]
            total_weight += w
            edge_count += 1
            if edge_count == n - 1:
                break

    if edge_count != n - 1:
        print("IMPOSSIBLE")
    else:
        print(f"{total_weight} {edge_count}")

if __name__ == "__main__":
    solve()
