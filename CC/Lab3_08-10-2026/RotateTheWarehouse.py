import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    g = [[int(data[1 + i * n + j]) for j in range(n)] for i in range(n)]
    
    for row in zip(*g[::-1]):
        print(*row)

if __name__ == "__main__":
    main()
