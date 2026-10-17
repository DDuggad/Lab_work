import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    if n == 0:
        print()
        return

    nums = data[1:1 + n]
    print(*nums[::-1])

if __name__ == "__main__":
    solve()
