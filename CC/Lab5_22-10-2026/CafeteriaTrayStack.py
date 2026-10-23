import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    cap = int(data[0])
    q = int(data[1])

    stack = []
    out = []
    p = 2
    for _ in range(q):
        op = data[p]
        if op == "PUSH":
            x = data[p + 1]
            if len(stack) == cap:
                out.append("FULL")
            else:
                stack.append(x)
            p += 2
        elif op == "POP":
            if not stack:
                out.append("EMPTY")
            else:
                out.append(stack.pop())
            p += 1
        elif op == "TOP":
            if not stack:
                out.append("EMPTY")
            else:
                out.append(stack[-1])
            p += 1
        elif op == "SIZE":
            out.append(str(len(stack)))
            p += 1

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
