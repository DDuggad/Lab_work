import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    src = int(data[2])
    dst = int(data[3])
    k = int(data[4])

    legs = []
    p = 5
    for _ in range(m):
        legs.append((int(data[p]), int(data[p + 1]), int(data[p + 2])))
        p += 3

    INF = float('inf')
    dp = [INF] * n
    dp[src] = 0

    best_cost = INF
    best_legs = -1

    for r in range(1, k + 2):
        next_dp = [INF] * n
        for u, v, w in legs:
            if dp[u] != INF:
                if dp[u] + w < next_dp[v]:
                    next_dp[v] = dp[u] + w
        dp = next_dp
        if dp[dst] < best_cost:
            best_cost = dp[dst]
            best_legs = r

    if best_cost == INF:
        print("-1 -1")
    else:
        print(f"{best_cost} {best_legs}")

if __name__ == "__main__":
    main()
