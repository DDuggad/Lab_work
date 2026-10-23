import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    a, b = data[0], data[1]
    m = len(b)
    b_list = list(b)
    stack = []

    for ch in a:
        stack.append(ch)
        if len(stack) >= m and stack[-m:] == b_list:
            del stack[-m:]

    ans = "".join(stack)
    print(ans if ans else "EMPTY")

if __name__ == "__main__":
    main()
