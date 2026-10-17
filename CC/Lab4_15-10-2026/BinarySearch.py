import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n, target = int(data[0]), int(data[1])
    nums = [int(x) for x in data[2:2 + n]]

    lo, hi = 0, n - 1
    ans = -1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            ans = mid
            break
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)

if __name__ == "__main__":
    solve()
