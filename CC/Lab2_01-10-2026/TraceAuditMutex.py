import sys

def main():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data[1:])
    held = {}
    for i, (a, t, m) in enumerate(zip(it, it, it), 1):
        if a == 'LOCK':
            if m in held:
                print(f"VIOLATION {i} {'REENTER' if held[m] == t else 'DOUBLE'}")
                return
            held[m] = t
        else:
            if m not in held:
                print(f"VIOLATION {i} UNHELD")
                return
            if held[m] != t:
                print(f"VIOLATION {i} FOREIGN")
                return
            del held[m]
    print(f"OK\n{len(held)}")
    for m in sorted(held):
        print(f"{m} {held[m]}")

if __name__ == '__main__':
    main()
