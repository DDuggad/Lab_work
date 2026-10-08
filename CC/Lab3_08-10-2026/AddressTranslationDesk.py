import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    P = int(data[0]); n = int(data[1]); q = int(data[2])
    frames = [int(x) for x in data[3:3 + n]]
    addrs = [int(x) for x in data[3 + n:3 + n + q]]
    
    limit = n * P
    for a in addrs:
        if a >= limit:
            print("SEGV")
        else:
            p = a // P
            offset = a % P
            f = frames[p]
            if f == -1:
                print(f"FAULT {p}")
            else:
                print(f * P + offset)

main()
