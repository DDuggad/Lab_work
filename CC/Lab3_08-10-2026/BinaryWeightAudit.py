import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    vals = [int(x) for x in data[1:1 + n]]
    
    bits = 0
    powers = 0
    
    for v in vals:
        c = bin(v).count('1')
        bits += c
        if c == 1:
            powers += 1
            
    print(f"{bits} {powers}")

if __name__ == "__main__":
    main()
