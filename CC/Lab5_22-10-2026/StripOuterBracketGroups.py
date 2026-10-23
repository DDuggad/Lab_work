import sys

def main():
    s = sys.stdin.readline().strip()
    if not s:
        print(0)
        print("EMPTY")
        return

    stack = []
    res = []
    groups = 0

    for ch in s:
        if ch in "([{":
            if stack:
                res.append(ch)
            else:
                groups += 1
            stack.append(ch)
        elif ch in ")]}":
            stack.pop()
            if stack:
                res.append(ch)
        else:
            res.append(ch)

    out_str = "".join(res) if res else "EMPTY"
    print(groups)
    print(out_str)

if __name__ == "__main__":
    main()
