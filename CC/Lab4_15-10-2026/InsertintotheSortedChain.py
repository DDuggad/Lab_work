import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    head = int(data[1])
    tail = int(data[2])

    value = [0] * n
    prv = [0] * n
    nxt = [0] * n
    p = 3
    for i in range(n):
        value[i] = int(data[p])
        prv[i] = int(data[p + 1])
        nxt[i] = int(data[p + 2])
        p += 3

    m = int(data[p])
    p += 1
    xs = [int(data[p + k]) for k in range(m)]

    for k, x in enumerate(xs):
        new_slot = n + k
        if head == -1:
            head = tail = new_slot
            value.append(x)
            prv.append(-1)
            nxt.append(-1)
        else:
            L = -1
            curr = head
            while curr != -1 and value[curr] <= x:
                L = curr
                curr = nxt[curr]

            value.append(x)
            if L == -1:
                prv.append(-1)
                nxt.append(head)
                prv[head] = new_slot
                head = new_slot
            elif L == tail:
                prv.append(tail)
                nxt.append(-1)
                nxt[tail] = new_slot
                tail = new_slot
            else:
                R = nxt[L]
                prv.append(L)
                nxt.append(R)
                nxt[L] = new_slot
                prv[R] = new_slot

    fwd_vals = []
    fwd_slots = []
    curr = head
    while curr != -1:
        fwd_vals.append(str(value[curr]))
        fwd_slots.append(str(curr))
        curr = nxt[curr]

    bwd_vals = []
    curr = tail
    while curr != -1:
        bwd_vals.append(str(value[curr]))
        curr = prv[curr]

    print(" ".join(fwd_vals))
    print(" ".join(bwd_vals))
    print(" ".join(fwd_slots))

if __name__ == "__main__":
    main()
