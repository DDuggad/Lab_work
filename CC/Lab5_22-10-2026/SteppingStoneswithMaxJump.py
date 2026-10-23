import sys
from collections import deque

def main():
    d = sys.stdin.read().split()
    if not d:
        return

    n = int(d[0])
    k = int(d[1])
    a = [int(x) for x in d[2:2 + n]]

    dp = [0] * n
    dp[0] = a[0]

    dq = deque([0])

    for i in range(1, n):
        # Remove indices out of window [i - k, i - 1]
        while dq and dq[0] < i - k:
            dq.popleft()

        # Maximum in window is at the front
        dp[i] = a[i] + dp[dq[0]]

        # Maintain decreasing order in deque
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()

        dq.append(i)

    print(dp[-1])

if __name__ == "__main__":
    main()
