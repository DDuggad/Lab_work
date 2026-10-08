import sys

def main():
    s = sys.stdin.readline().strip()
    if not s:
        return
    res = []
    i = 0
    n = len(s)
    while i < n:
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        res.append(s[i] + str(j - i))
        i = j
    print("".join(res))

if __name__ == "__main__":
    main()
