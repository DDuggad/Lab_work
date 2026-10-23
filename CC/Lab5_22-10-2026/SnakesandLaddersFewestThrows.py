import sys
from collections import deque

def main():
    d = sys.stdin.read().split()
    if not d:
        return

    N = int(d[0])
    m = int(d[1])

    jump = [0] * (N + 1)
    idx = 2
    for _ in range(m):
        u = int(d[idx])
        v = int(d[idx + 1])
        jump[u] = v
        idx += 2

    dist = [-1] * (N + 1)
    dist[1] = 0
    q = deque([1])

    while q:
        curr = q.popleft()

        if curr == N:
            print(dist[curr])
            return

        for r in range(1, 7):
            nxt = curr + r
            if nxt > N:
                continue

            # Take snake or ladder if present
            dest = jump[nxt] if jump[nxt] != 0 else nxt

            if dist[dest] == -1:
                dist[dest] = dist[curr] + 1
                q.append(dest)

    print(-1)

if __name__ == "__main__":
    main()
