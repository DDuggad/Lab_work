import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    free_cache = {}

    def get_free(k):
        if k in free_cache:
            return free_cache[k]
        dp = [[0] * k for _ in range(20)]
        dp[0][0] = 1
        for length in range(1, 20):
            prev = dp[length - 1]
            curr = dp[length]
            for rem in range(k):
                ways = 0
                for d in range(10):
                    ways += prev[(rem + d) % k]
                curr[rem] = ways
        free_cache[k] = dp
        return dp

    out = []
    p = 1
    for _ in range(q):
        n = int(data[p])
        k = int(data[p + 1])
        p += 2
        if k == 1:
            out.append(str(n))
            continue
        digits = [int(ch) for ch in str(n)]
        L = len(digits)
        dp = get_free(k)
        ans = 0
        rem = 0
        for i, limit in enumerate(digits):
            rem_len = L - 1 - i
            for d in range(limit):
                ans += dp[rem_len][(rem + d) % k]
            rem = (rem + limit) % k
        if rem == 0:
            ans += 1
        out.append(str(ans - 1))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
