import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    R = int(data[0]); C = int(data[1])
    
    idx = 2
    row_sums = []
    col_sums = [0] * C
    
    for _ in range(R):
        row = [int(x) for x in data[idx:idx + C]]
        idx += C
        row_sums.append(sum(row))
        for j in range(C):
            col_sums[j] += row[j]
            
    print(*(row_sums))
    print(*(col_sums))
    print(sum(row_sums))

if __name__ == "__main__":
    main()
