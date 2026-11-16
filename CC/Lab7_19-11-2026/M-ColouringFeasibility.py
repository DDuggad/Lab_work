import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    V, E = int(data[0]), int(data[1])
    adj = [set() for _ in range(V)]
    has_self_loop = False
    for i in range(E):
        u = int(data[2 + 2 * i])
        v = int(data[3 + 2 * i])
        if u == v:
            has_self_loop = True
        adj[u].add(v)
        adj[v].add(u)
    M = int(data[2 + 2 * E])

    if has_self_loop:
        print("NO")
        return

    if M >= V:
        print("YES")
        return

    order = sorted(range(V), key=lambda x: len(adj[x]), reverse=True)
    color = [-1] * V

    def dfs(idx, max_used):
        if idx == V:
            return True
        u = order[idx]
        used = {color[v] for v in adj[u] if color[v] != -1}
        for c in range(min(M, max_used + 2)):
            if c not in used:
                color[u] = c
                if dfs(idx + 1, max(max_used, c)):
                    return True
                color[u] = -1
        return False

    print("YES" if dfs(0, -1) else "NO")

if __name__ == "__main__":
    main()
