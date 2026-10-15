import sys
import heapq

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    top1, top2 = heapq.nlargest(2, map(int, tokens[1:]))

    print(top1 + top2)
    print(top1, top2)

if __name__ == "__main__":
    main()
