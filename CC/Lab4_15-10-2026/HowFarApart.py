import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    head = int(data[1])

    nxt = [0] * n
    p = 3
    for i in range(n):
        nxt[i] = int(data[p + 2])
        p += 3

    pos = [0] * n
    curr = head
    idx = 0
    while curr != -1:
        pos[curr] = idx
        idx += 1
        curr = nxt[curr]

    q = int(data[p])
    p += 1

    out = []
    for _ in range(q):
        a = int(data[p])
        b = int(data[p + 1])
        p += 2
        out.append(str(pos[b] - pos[a]))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
