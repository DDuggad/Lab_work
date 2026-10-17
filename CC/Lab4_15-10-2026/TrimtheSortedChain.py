import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    n = int(data[0])
    head = int(data[1])
    tail = int(data[2])

    value = [0] * n
    nxt = [0] * n
    p = 3
    for i in range(n):
        value[i] = int(data[p])
        nxt[i] = int(data[p + 2])
        p += 3

    lo = int(data[p])
    hi = int(data[p + 1])

    chain = []
    curr = head
    while curr != -1:
        chain.append((value[curr], curr))
        curr = nxt[curr]

    surviving = [item for item in chain if lo <= item[0] <= hi]

    if not surviving:
        print("0 -1 -1")
        return

    m = len(surviving)
    new_head = surviving[0][1]
    new_tail = surviving[-1][1]

    fwd_slots = [item[1] for item in surviving]
    bwd_slots = fwd_slots[::-1]
    fwd_vals = [item[0] for item in surviving]

    print(f"{m} {new_head} {new_tail}")
    print(*fwd_slots)
    print(*bwd_slots)
    print(*fwd_vals)

if __name__ == "__main__":
    main()
