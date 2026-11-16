import sys

def count_ways(n):
    if n == 0:
        return 1
    full = (1 << n) - 1

    def dfs(cols, d1, d2):
        if cols == full:
            return 1
        total = 0
        avail = full & ~(cols | d1 | d2)
        while avail:
            bit = avail & -avail
            avail -= bit
            total += dfs(cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1)
        return total

    total = 0
    for c in range(n // 2):
        bit = 1 << c
        total += 2 * dfs(bit, bit << 1, bit >> 1)

    if n % 2 == 1:
        bit = 1 << (n // 2)
        total += dfs(bit, bit << 1, bit >> 1)

    return total

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    q = int(data[0])
    cache = {}
    out = []
    for i in range(1, q + 1):
        n = int(data[i])
        if n not in cache:
            cache[n] = count_ways(n)
        out.append(str(cache[n]))
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
