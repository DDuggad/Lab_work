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

    chain_slots = []
    chain_vals = []
    curr = head
    while curr != -1:
        chain_slots.append(curr)
        chain_vals.append(value[curr])
        curr = nxt[curr]

    half_idx = len(chain_slots) // 2
    half_slot = chain_slots[half_idx]
    half_val = chain_vals[half_idx]

    print(f"{half_slot} {half_val}")
    print(*chain_vals[half_idx:])

if __name__ == "__main__":
    main()
