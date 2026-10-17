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

    q = int(data[p])
    p += 1
    reqs = [(int(data[p + 2 * i]), int(data[p + 2 * i + 1])) for i in range(q)]

    total_cost = 0

    for x, c in reqs:
        curr = head
        pos = 1
        found_slot = -1
        while curr != -1:
            if value[curr] == x:
                found_slot = curr
                break
            curr = nxt[curr]
            pos += 1

        if found_slot != -1:
            total_cost += c * pos
            if found_slot != head:
                p_node = prv[found_slot]
                nx_node = nxt[found_slot]
                nxt[p_node] = nx_node
                if nx_node != -1:
                    prv[nx_node] = p_node
                else:
                    tail = p_node

                prv[found_slot] = -1
                nxt[found_slot] = head
                prv[head] = found_slot
                head = found_slot
        else:
            total_cost += c * n

    fwd_slots = []
    fwd_vals = []
    curr = head
    while curr != -1:
        fwd_slots.append(str(curr))
        fwd_vals.append(str(value[curr]))
        curr = nxt[curr]

    bwd_slots = []
    curr = tail
    while curr != -1:
        bwd_slots.append(str(curr))
        curr = prv[curr]

    print(total_cost)
    print(" ".join(fwd_slots))
    print(" ".join(fwd_vals))
    print(" ".join(bwd_slots))

if __name__ == "__main__":
    main()
