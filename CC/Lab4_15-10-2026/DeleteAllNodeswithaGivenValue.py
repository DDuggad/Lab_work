import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    values = data[1:1 + n]
    x = data[1 + n]

    filtered = [v for v in values if v != x]

    if not filtered:
        print("EMPTY")
    else:
        print(*filtered)

if __name__ == "__main__":
    main()
