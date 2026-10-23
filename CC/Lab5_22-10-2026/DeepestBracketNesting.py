import sys

def main():
    s = sys.stdin.readline().strip()
    if not s:
        print(0)
        print("NONE")
        return

    open_brackets = set("([{")
    close_brackets = set(")]}")

    max_depth = 0
    best_idx = -1
    curr_depth = 0

    # Pass 1: Find max depth and the index where it was first reached
    for i, ch in enumerate(s):
        if ch in open_brackets:
            curr_depth += 1
            if curr_depth > max_depth:
                max_depth = curr_depth
                best_idx = i
        elif ch in close_brackets:
            curr_depth -= 1

    if max_depth == 0:
        print(0)
        print("NONE")
        return

    # Pass 2: Reconstruct the stack only once up to best_idx
    stack = []
    for ch in s[:best_idx + 1]:
        if ch in open_brackets:
            stack.append(ch)
        elif ch in close_brackets:
            stack.pop()

    print(max_depth)
    print("".join(stack))

if __name__ == "__main__":
    main()
