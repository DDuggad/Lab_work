import sys
from collections import Counter

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    skus = [int(x) for x in data[1:1 + n]]
    
    counts = Counter(skus)
    ans = min(counts.keys(), key=lambda x: (-counts[x], x))
    
    print(ans)

if __name__ == "__main__":
    main()
