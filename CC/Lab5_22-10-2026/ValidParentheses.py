import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        print("true")
        return

    mapping = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                print("false")
                return
        else:
            stack.append(char)

    if not stack:
        print("true")
    else:
        print("false")

if __name__ == "__main__":
    solve()
