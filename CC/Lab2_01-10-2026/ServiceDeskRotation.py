import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, k = int(data[0]), int(data[1])
    units = [int(x) for x in data[2:2 + n]]

    tickets = [((u + k - 1) // k, i + 1) for i, u in enumerate(units)]
    tickets.sort()

    print(*(idx for _, idx in tickets))

if __name__ == "__main__":
    main()
