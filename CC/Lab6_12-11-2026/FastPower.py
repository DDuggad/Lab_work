import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    q = int(data[0])
    MOD = 1000000007
    out = []

    for i in range(q):
        x = int(data[1 + 2 * i])
        n = int(data[2 + 2 * i])
        ans = 1
        x %= MOD
        while n > 0:
            if n % 2 == 1:
                ans = (ans * x) % MOD
            x = (x * x) % MOD
            n //= 2
        out.append(str(ans))

    print("\n".join(out))

if __name__ == "__main__":
    main()
