import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); q = int(data[idx + 1]); idx += 2
    
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
            'rem': burst,
            'orig_idx': i,
            'comp': 0
        })
        
    sorted_procs = sorted(procs, key=lambda p: (p['arrival'], p['orig_idx']))
    
    ready_queue = deque()
    t = 0
    unarrived_idx = 0
    dispatches = 0
    
    while unarrived_idx < n or ready_queue:
        if not ready_queue and unarrived_idx < n:
            if t < sorted_procs[unarrived_idx]['arrival']:
                t = sorted_procs[unarrived_idx]['arrival']
            while unarrived_idx < n and sorted_procs[unarrived_idx]['arrival'] <= t:
                ready_queue.append(sorted_procs[unarrived_idx])
                unarrived_idx += 1
                
        curr = ready_queue.popleft()
        dispatches += 1
        
        exec_time = min(q, curr['rem'])
        t += exec_time
        curr['rem'] -= exec_time
        
        while unarrived_idx < n and sorted_procs[unarrived_idx]['arrival'] <= t:
            ready_queue.append(sorted_procs[unarrived_idx])
            unarrived_idx += 1
            
        if curr['rem'] > 0:
            ready_queue.append(curr)
        else:
            curr['comp'] = t

    for p in procs:
        comp = p['comp']
        tat = comp - p['arrival']
        wt = tat - p['burst']
        print(f"{p['pid']} {comp} {tat} {wt}")
        
    print(dispatches)

if __name__ == "__main__":
    main()
