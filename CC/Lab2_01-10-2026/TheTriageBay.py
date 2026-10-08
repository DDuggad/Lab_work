import sys
import heapq

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

    # Sort processes by arrival time and original input position
    sorted_procs = sorted(procs, key=lambda p: (p['arrival'], p['orig_idx']))
    
    # Ready queue key: (burst, arrival, orig_idx)
    ready = []
    
    t = 0
    i = 0
    completed = 0
    
    while completed < n:
        # Jump time if CPU is idle and no processes are in ready queue
        if not ready and i < n and t < sorted_procs[i]['arrival']:
            t = sorted_procs[i]['arrival']
            
        # Enqueue all processes that arrived at or before current time t
        while i < n and sorted_procs[i]['arrival'] <= t:
            p = sorted_procs[i]
            heapq.heappush(ready, (p['burst'], p['arrival'], p['orig_idx'], p))
            i += 1
            
        # Select shortest job and run to completion
        burst, arrival, orig_idx, curr = heapq.heappop(ready)
        t += burst
        curr['comp'] = t
        completed += 1

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
