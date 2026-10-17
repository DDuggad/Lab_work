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

    chain_val = []
    chain_slot = []
    curr = head
    while curr != -1:
        chain_val.append(value[curr])
        chain_slot.append(curr)
        curr = nxt[curr]

    runs = []
    for v, s in zip(chain_val, chain_slot):
        if not runs or runs[-1][0] != v:
            runs.append((v, s))

    hills = []
    valleys = []
    for i in range(1, len(runs) - 1):
        left_v = runs[i - 1][0]
        curr_v, slot = runs[i]
        right_v = runs[i + 1][0]

        if curr_v > left_v and curr_v > right_v:
            hills.append(slot)
        elif curr_v < left_v and curr_v < right_v:
            valleys.append(slot)

    print(f"{len(hills)} {len(valleys)}")
    print(*hills)
    print(*valleys)

if __name__ == "__main__":
    main()
