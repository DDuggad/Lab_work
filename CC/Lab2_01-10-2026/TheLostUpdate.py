import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    T = int(data[idx]); x = int(data[idx + 1]); idx += 2
    progs = []
    for _ in range(T):
        k = int(data[idx]); idx += 1
        progs.append(data[idx:idx + k]); idx += k
    m = int(data[idx]); idx += 1
    sched = [int(v) for v in data[idx:idx + m]]
    
    ip = [0] * T
    r = [0] * T
    last_load_time = [-1] * T
    last_other_store_time = [-1] * T
    stale_stores = 0
    
    for step in range(m):
        t = sched[step] - 1
        instr = progs[t][ip[t]]
        ip[t] += 1
        
        if instr == "L":
            r[t] = x
            last_load_time[t] = step
        elif instr == "S":
            x = r[t]
            if last_other_store_time[t] > last_load_time[t]:
                stale_stores += 1
            for other in range(T):
                if other != t:
                    last_other_store_time[other] = step
        else:
            r[t] += int(instr)
            
    print(x)
    print(stale_stores)

if __name__ == "__main__":
    main()
