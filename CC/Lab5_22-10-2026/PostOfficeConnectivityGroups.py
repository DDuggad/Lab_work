import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    x = int(data[1])
    p = [int(val) for val in data[2:2 + n]]

    p.sort()

    num_groups = 1
    curr_size = 1
    max_size = 1

    for i in range(1, n):
        if p[i] - p[i - 1] <= x:
            curr_size += 1
        else:
            num_groups += 1
            if curr_size > max_size:
                max_size = curr_size
            curr_size = 1

    if curr_size > max_size:
        max_size = curr_size

    print(num_groups)
    print(max_size)

if __name__ == "__main__":
    main()
