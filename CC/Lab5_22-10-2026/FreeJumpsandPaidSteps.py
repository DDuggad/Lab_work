import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = int(input_data[0])
    q = int(input_data[1])
    targets = [int(x) for x in input_data[2:2 + q]]

    LIMIT = 200000
    dist = [-1] * (LIMIT + 1)
    dist[s] = 0

    dq = deque([s])

    while dq:
        u = dq.popleft()
        d = dist[u]

        # Cost 0 move: tailwind jump to 2x
        v = 2 * u
        if 0 < v <= LIMIT:
            if dist[v] == -1 or dist[v] > d:
                dist[v] = d
                dq.appendleft(v)

        # Cost 1 move: step left to u - 1
        v = u - 1
        if v >= 0:
            if dist[v] == -1 or dist[v] > d + 1:
                dist[v] = d + 1
                dq.append(v)

        # Cost 1 move: step right to u + 1
        v = u + 1
        if v <= LIMIT:
            if dist[v] == -1 or dist[v] > d + 1:
                dist[v] = d + 1
                dq.append(v)

    output = [str(dist[t]) for t in targets]
    print("\n".join(output))

if __name__ == "__main__":
    main()
