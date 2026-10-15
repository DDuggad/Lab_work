import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n, k = int(data[0]), int(data[1])
    a = data[2:2 + n]

    k %= n
    idx = n - k
    rotated = a[idx:] + a[:idx]

    print(*rotated)

if __name__ == "__main__":
    main()
