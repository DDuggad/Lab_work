import sys
import math

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    vals = [int(x) for x in data[1:1 + n]]
    
    g = vals[0]
    l = vals[0]
    
    for v in vals[1:]:
        g = math.gcd(g, v)
        l = (l // math.gcd(l, v)) * v
        
    print(f"{g} {l}")

if __name__ == "__main__":
    main()
