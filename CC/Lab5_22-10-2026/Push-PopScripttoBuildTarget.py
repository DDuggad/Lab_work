import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    k = int(data[1])
    target = [int(x) for x in data[2:2 + k]]

    pushes = target[-1]
    pops = target[-1] - k

    script = []
    prev = 0
    for val in target:
        skipped = val - prev - 1
        if skipped > 0:
            script.append("+-" * skipped)
        script.append("+")
        prev = val

    s = "".join(script)
    print(f"{pushes} {pops}")
    print(s)

if __name__ == "__main__":
    main()
