import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    ns = [int(x) for x in data[1:1 + q]]
    max_n = max(ns)
    dp = [1, 1, 2]
    if max_n >= 3:
        a, b, c = 1, 1, 2
        MOD = 1000000007
        dp_app = dp.append
        for _ in range(3, max_n + 1, 3):
            d = (a + b + c) % MOD
            e = (b + c + d) % MOD
            f = (c + d + e) % MOD
            dp_app(d); dp_app(e); dp_app(f)
            a, b, c = d, e, f
    sys.stdout.write("\n".join(str(dp[n]) for n in ns) + "\n")
if __name__ == "__main__":
    main()
