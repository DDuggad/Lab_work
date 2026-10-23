import sys

def solve(s):
    l, r = 0, len(s) - 1
    res = []
    while l <= r:
        if s[l:r+1] < s[l:r+1][::-1]:
            res.append(s[l])
            l += 1
        else:
            res.append(s[r])
            r -= 1
    return "".join(res)

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    out = [solve(data[1 + k]) for k in range(t)]
    print("\n".join(out))

if __name__ == "__main__":
    main()
