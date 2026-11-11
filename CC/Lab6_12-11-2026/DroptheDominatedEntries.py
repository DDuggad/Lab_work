import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n, head, tail = int(data[0]), int(data[1]), int(data[2])
    value = [0] * n
    prv = [0] * n
    nxt = [0] * n
    p = 3
    for i in range(n):
        value[i] = int(data[p])
        prv[i] = int(data[p + 1])
        nxt[i] = int(data[p + 2])
        p += 3

    curr = tail
    max_val = float('-inf')
    while curr != -1:
        prev_node = prv[curr]
        if value[curr] < max_val:
            a, b = prv[curr], nxt[curr]
            if a != -1:
                nxt[a] = b
            else:
                head = b
            if b != -1:
                prv[b] = a
        else:
            max_val = value[curr]
        curr = prev_node

    f_slots, f_vals = [], []
    curr = head
    while curr != -1:
        f_slots.append(str(curr))
        f_vals.append(str(value[curr]))
        curr = nxt[curr]

    b_slots = []
    curr = tail
    while curr != -1:
        b_slots.append(str(curr))
        curr = prv[curr]

    print(len(f_slots))
    print(" ".join(f_slots))
    print(" ".join(b_slots))
    print(" ".join(f_vals))

if __name__ == "__main__":
    main()
