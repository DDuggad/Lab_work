import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    n = int(data[0])
    iv = []
    for i in range(n):
        iv.append((int(data[1 + 2 * i]), int(data[2 + 2 * i])))
    iv.sort()
    merged = []
    cs, ce = iv[0]
    for s, e in iv[1:]:
        if s <= ce:
            ce = max(ce, e)
        else:
            merged.append((cs, ce))
            cs, ce = s, e
    merged.append((cs, ce))
    print(len(merged))
    for s, e in merged:
        print(f"{s} {e}")

if __name__ == "__main__":
    main()
