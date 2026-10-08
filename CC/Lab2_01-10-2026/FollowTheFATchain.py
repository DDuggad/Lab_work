import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    q = int(data[1])
    fat = [int(x) for x in data[2:2 + n]]
    starts = [int(x) for x in data[2 + n:2 + n + q]]
    
    reachable = set()
    
    for start in starts:
        b = start
        chain = []
        visited_in_chain = set()
        error = None
        
        while True:
            if b < 0 or b >= n:
                error = "RANGE"
                break
            if fat[b] == -2:
                error = f"FREE {b}"
                break
            if b in visited_in_chain:
                error = "LOOP"
                break
            
            chain.append(b)
            visited_in_chain.add(b)
            reachable.add(b)
            
            if fat[b] == -1:
                break
            b = fat[b]
            
        if error:
            print(error)
        else:
            print(f"{len(chain)} " + " ".join(map(str, chain)))
            
    lost = sum(1 for i in range(n) if fat[i] != -2 and i not in reachable)
    print(lost)

if __name__ == "__main__":
    main()
