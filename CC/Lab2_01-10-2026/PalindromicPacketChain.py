import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    n = int(data[0])
    head = int(data[1])
    
    value = [0] * n
    nxt = [0] * n
    p = 2
    for i in range(n):
        value[i] = int(data[p])
        nxt[i] = int(data[p + 1])
        p += 2

    # Traverse chain from head
    chain = []
    curr = head
    while curr != -1:
        chain.append(value[curr])
        curr = nxt[curr]

    # Check palindrome
    is_palindrome = (chain == chain[::-1])
    mid_val = chain[len(chain) // 2]

    print("YES" if is_palindrome else "NO")
    print(mid_val)

if __name__ == "__main__":
    main()
