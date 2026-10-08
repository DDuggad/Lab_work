import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0]); start = int(data[1])
    movements = [int(x) for x in data[2:2 + n]]
    
    curr = start
    low = start
    
    for m in movements:
        curr += m
        if curr < low:
            low = curr
            
    print(f"{curr} {low}")

if __name__ == "__main__":
    main()
