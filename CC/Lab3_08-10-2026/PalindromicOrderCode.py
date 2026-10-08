import sys

def main():
    line = sys.stdin.readline()
    cleaned = [c.lower() for c in line if c.isalnum()]
    if cleaned == cleaned[::-1]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
