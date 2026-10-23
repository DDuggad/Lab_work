import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]

    i = 0
    while i < n:
        j = i
        bc = a[i].bit_count()
        while j < n and a[j].bit_count() == bc:
            j += 1
        a[i:j] = sorted(a[i:j])
        i = j

    for i in range(n - 1):
        if a[i] > a[i + 1]:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    main()
