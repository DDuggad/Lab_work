import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0]); m = int(data[1])
    shelf = [int(x) for x in data[2:2 + n]]
    tray = [int(x) for x in data[2 + n:2 + n + m]]
    shelf.extend([0] * m)   # the m spare slots at the end of the shelf

    i = n - 1
    j = m - 1
    write = n + m - 1

    # Merge from back to front
    while j >= 0:
        if i >= 0 and shelf[i] > tray[j]:
            shelf[write] = shelf[i]
            i -= 1
        else:
            shelf[write] = tray[j]
            j -= 1
        write -= 1

    print(*shelf)

if __name__ == "__main__":
    main()
