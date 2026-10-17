import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    pos = int(data[1])
    
    if pos != -1:
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    solve()
