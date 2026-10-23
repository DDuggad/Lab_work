import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    sorted_a = sorted(a)

    pivot = a[-1]
    i = -1
    for j in range(n - 1):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]

    p_idx = i + 1
    a[p_idx], a[-1] = a[-1], a[p_idx]

    print(p_idx)
    print(*a)
    print(*sorted_a)

if __name__ == "__main__":
    main()
