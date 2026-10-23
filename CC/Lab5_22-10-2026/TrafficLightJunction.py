import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n, g0, g1 = data[0], data[1], data[2]
    a = data[3:3 + n]
    ln = data[3 + n:3 + 2 * n]

    q = [deque(), deque()]
    ans = [0] * n

    t = 0
    car_idx = 0
    cycle = g0 + g1
    processed = 0

    while processed < n:
        if not q[0] and not q[1] and car_idx < n and t < a[car_idx]:
            t = a[car_idx]

        while car_idx < n and a[car_idx] <= t:
            q[ln[car_idx]].append(car_idx)
            car_idx += 1

        green = 0 if (t % cycle) < g0 else 1
        if q[green]:
            c = q[green].popleft()
            ans[c] = t
            processed += 1

        t += 1

    print(*ans)

if __name__ == "__main__":
    main()
