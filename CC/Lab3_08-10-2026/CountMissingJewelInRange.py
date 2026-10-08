import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    arr = [int(x) for x in data]
    unique = set(arr)
    ans = (max(unique) - min(unique) + 1) - len(unique)
    print(ans)

if __name__ == "__main__":
    solve()
