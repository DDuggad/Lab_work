import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    
    procs = []
    for i in range(n):
        pid = data[idx]
        arrival = int(data[idx + 1])
        burst = int(data[idx + 2])
        idx += 3
        procs.append({
            'pid': pid,
            'arrival': arrival,
            'burst': burst,
            'orig_idx': i,
            'comp': 0
        })

    # Sort processes by arrival time, using original index as tie-breaker
    sorted_procs = sorted(procs, key=lambda p: (p['arrival'], p['orig_idx']))
    
    t = 0
    for p in sorted_procs:
        if t < p['arrival']:
            t = p['arrival']
        t += p['burst']
        p['comp'] = t

    total_wt = 0
    total_tat = 0
    
    for p in procs:
        comp = p['comp']
        tat = comp - p['arrival']
        wt = tat - p['burst']
        total_wt += wt
        total_tat += tat
        print(f"{p['pid']} {comp} {tat} {wt}")
        
    avg_wt = total_wt / n
    avg_tat = total_tat / n
    print(f"{avg_wt:.4f} {avg_tat:.4f}")

if __name__ == "__main__":
    main()
