import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    arr = [int(x) for x in data[1:1 + n]]
    x = int(data[1 + n])

    lo, hi = 0, n - 1
    ans = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            ans = mid
            break
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)

if __name__ == "__main__":
    solve()
