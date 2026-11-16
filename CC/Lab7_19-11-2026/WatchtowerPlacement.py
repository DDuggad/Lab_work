import sys

sys.setrecursionlimit(10000)

def count_ways(n):
    cols = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)

    def dfs(r):
        if r == n:
            return 1
        total = 0
        for c in range(n):
            d1 = r - c + n - 1
            d2 = r + c
            if not cols[c] and not diag1[d1] and not diag2[d2]:
                cols[c] = diag1[d1] = diag2[d2] = True
                total += dfs(r + 1)
                cols[c] = diag1[d1] = diag2[d2] = False
        return total

    return dfs(0)

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    table = [count_ways(i) for i in range(13)]
    q = int(data[0])
    out = [str(table[int(data[i + 1])]) for i in range(q)]
    print("\n".join(out))

if __name__ == "__main__":
    main()
