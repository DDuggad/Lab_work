import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    tokens = data[1:1 + n]

    stack = []
    for token in tokens:
        if token == "+":
            stack.append(stack[-1] + stack[-2])
        elif token == "D":
            stack.append(stack[-1] * 2)
        elif token == "C":
            stack.pop()
        else:
            stack.append(int(token))

    print(len(stack))
    print(sum(stack))

if __name__ == "__main__":
    main()
