import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0]); head = int(data[1]); cyl = int(data[2])
    reqs = [int(x) for x in data[3:3 + n]]
    
    total = 0
    reversals = 0
    last_dir = 0
    curr = head
    
    for r in reqs:
        diff = r - curr
        total += abs(diff)
        curr_dir = 1 if diff > 0 else (-1 if diff < 0 else 0)
        if curr_dir != 0:
            if last_dir != 0 and curr_dir != last_dir:
                reversals += 1
            last_dir = curr_dir
        curr = r

    print(total)
    print(reversals)

main()
