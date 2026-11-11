import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]

    cur = a[0]
    best = a[0]

    for val in a[1:]:
        cur = max(val, cur + val)
        best = max(best, cur)

    print(best)

if __name__ == "__main__":
    main()
