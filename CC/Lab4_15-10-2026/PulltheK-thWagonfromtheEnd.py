import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    head = int(data[1])

    value = [0] * n
    nxt = [0] * n
    p = 2
    for i in range(n):
        value[i] = int(data[p])
        nxt[i] = int(data[p + 1])
        p += 2

    k = int(data[p])

    chain_slots = []
    chain_vals = []
    curr = head
    while curr != -1:
        chain_slots.append(curr)
        chain_vals.append(value[curr])
        curr = nxt[curr]

    target_idx = len(chain_slots) - k
    removed_slot = chain_slots[target_idx]
    removed_val = chain_vals[target_idx]

    print(f"{removed_slot} {removed_val}")

    remaining_vals = chain_vals[:target_idx] + chain_vals[target_idx + 1:]
    if not remaining_vals:
        print("EMPTY")
    else:
        print(*remaining_vals)

if __name__ == "__main__":
    main()
