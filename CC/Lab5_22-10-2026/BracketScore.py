import sys

def main():
    s = sys.stdin.readline().strip()
    if not s:
        return
    MOD = 10**9 + 7
    stack = [0]
    for ch in s:
        if ch in "([":
            stack.append(0)
        else:
            val = stack.pop()
            multiplier = 2 if ch == ')' else 3
            score = 1 if val == 0 else (val * multiplier) % MOD
            stack[-1] = (stack[-1] + score) % MOD
    print(stack[0])

if __name__ == "__main__":
    main()
