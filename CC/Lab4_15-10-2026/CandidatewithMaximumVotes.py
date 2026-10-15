import sys
from collections import Counter

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    counts = Counter(data[1:])
    winner = max(sorted(counts.keys()), key=counts.get)

    print(f"{winner} {counts[winner]}")

if __name__ == "__main__":
    main()
