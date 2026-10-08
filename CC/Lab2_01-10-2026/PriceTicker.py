import sys

def main():
    tok = sys.stdin.read().split()
    if not tok:
        return

    out = []
    val_stack = []
    min_stack = []

    if tok[0] == "GEN":
        q = int(tok[1])
        seed = int(tok[2])
        x = seed

        for _ in range(q):
            x = (x * 1103515245 + 12345) % (1 << 31)
            op = x % 16

            if op <= 9:  # PUSH
                v = (x // 256) % 100000
                val_stack.append(v)
                if not min_stack:
                    min_stack.append(v)
                else:
                    min_stack.append(min(v, min_stack[-1]))
            elif op in (10, 11):  # POP
                if not val_stack:
                    out.append("EMPTY")
                else:
                    val_stack.pop()
                    min_stack.pop()
            elif op in (12, 13):  # MIN
                if not min_stack:
                    out.append("EMPTY")
                else:
                    out.append(str(min_stack[-1]))
            elif op in (14, 15):  # TOP
                if not val_stack:
                    out.append("EMPTY")
                else:
                    out.append(str(val_stack[-1]))
    else:
        q = int(tok[0])
        idx = 1
        for _ in range(q):
            cmd = tok[idx]
            if cmd == "PUSH":
                v = int(tok[idx + 1])
                idx += 2
                val_stack.append(v)
                if not min_stack:
                    min_stack.append(v)
                else:
                    min_stack.append(min(v, min_stack[-1]))
            elif cmd == "POP":
                idx += 1
                if not val_stack:
                    out.append("EMPTY")
                else:
                    val_stack.pop()
                    min_stack.pop()
            elif cmd == "MIN":
                idx += 1
                if not min_stack:
                    out.append("EMPTY")
                else:
                    out.append(str(min_stack[-1]))
            elif cmd == "TOP":
                idx += 1
                if not val_stack:
                    out.append("EMPTY")
                else:
                    out.append(str(val_stack[-1]))

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))

if __name__ == "__main__":
    main()
