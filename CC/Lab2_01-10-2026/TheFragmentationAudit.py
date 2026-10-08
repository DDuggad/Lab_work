import sys

def simulate(M, ops, policy):
    holes = [(0, M)]
    allocated = {}
    fails = 0

    for op in ops:
        if op[0] == "A":
            _, id_, size = op
            eligible = [h for h in holes if h[1] >= size]
            if not eligible:
                fails += 1
            else:
                if policy == "BEST":
                    chosen = min(eligible, key=lambda h: (h[1], h[0]))
                else:  # WORST
                    chosen = max(eligible, key=lambda h: (h[1], -h[0]))

                h_start, h_size = chosen
                holes.remove(chosen)
                allocated[id_] = (h_start, size)

                rem_size = h_size - size
                if rem_size > 0:
                    holes.append((h_start + size, rem_size))
                    holes.sort(key=lambda x: x[0])

        elif op[0] == "F":
            _, id_ = op
            if id_ in allocated:
                start, size = allocated.pop(id_)
                holes.append((start, size))
                holes.sort(key=lambda x: x[0])

                merged = []
                for h in holes:
                    if not merged:
                        merged.append(h)
                    else:
                        last_s, last_sz = merged[-1]
                        if last_s + last_sz == h[0]:
                            merged[-1] = (last_s, last_sz + h[1])
                        else:
                            merged.append(h)
                holes = merged

    total_free = sum(h[1] for h in holes)
    max_hole = max((h[1] for h in holes), default=0)
    frag = total_free - max_hole
    return fails, frag

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    M = int(data[0])
    q = int(data[1])
    ops = []
    idx = 2
    for _ in range(q):
        if data[idx] == "A":
            ops.append(("A", data[idx + 1], int(data[idx + 2])))
            idx += 3
        else:
            ops.append(("F", data[idx + 1]))
            idx += 2

    best_fails, best_frag = simulate(M, ops, "BEST")
    worst_fails, worst_frag = simulate(M, ops, "WORST")

    print(f"BEST {best_fails} {best_frag}")
    print(f"WORST {worst_fails} {worst_frag}")

if __name__ == "__main__":
    main()
