import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    M = int(data[0])
    q = int(data[1])
    
    holes = [(0, M)]
    allocated = {}
    
    idx = 2
    for _ in range(q):
        op = data[idx]
        if op == "A":
            ident = data[idx + 1]
            size = int(data[idx + 2])
            idx += 3
            
            placed_idx = -1
            for i, (h_start, h_size) in enumerate(holes):
                if h_size >= size:
                    placed_idx = i
                    break
            
            if placed_idx != -1:
                h_start, h_size = holes[placed_idx]
                allocated[ident] = (h_start, size)
                print(f"{ident} {h_start}")
                
                rem_size = h_size - size
                if rem_size > 0:
                    holes[placed_idx] = (h_start + size, rem_size)
                else:
                    holes.pop(placed_idx)
            else:
                print(f"{ident} FAIL")
                
        elif op == "F":
            ident = data[idx + 1]
            idx += 2
            
            if ident in allocated:
                start, size = allocated.pop(ident)
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

    num_holes = len(holes)
    largest_hole = max((sz for _, sz in holes), default=0)
    print(f"{num_holes} {largest_hole}")

if __name__ == "__main__":
    main()
