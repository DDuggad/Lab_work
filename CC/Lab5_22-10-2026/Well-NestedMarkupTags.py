import sys

def check(doc):
    stack = []
    tag_count = 0
    i = 0
    n = len(doc)
    while i < n:
        if doc[i] == '<':
            j = doc.find('>', i)
            tag = doc[i+1:j]
            tag_count += 1
            if tag.startswith('/'):
                if not stack or stack[-1] != tag[1:]:
                    return f"MISMATCH {tag_count}"
                stack.pop()
            else:
                stack.append(tag)
            i = j
        i += 1
    return f"UNCLOSED {len(stack)}" if stack else "VALID"

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    t = int(lines[0])
    for i in range(1, t + 1):
        print(check(lines[i]))

if __name__ == "__main__":
    main()
