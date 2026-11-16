import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    R, C = int(data[0]), int(data[1])
    grid = [list(row) for row in data[2:2 + R]]
    word = data[2 + R]

    if len(word) > R * C:
        print("NO")
        return

    def dfs(r, c, idx):
        if grid[r][c] != word[idx]:
            return False
        if idx == len(word) - 1:
            return True
        tmp = grid[r][c]
        grid[r][c] = "#"
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#":
                if dfs(nr, nc, idx + 1):
                    grid[r][c] = tmp
                    return True
        grid[r][c] = tmp
        return False

    for r in range(R):
        for c in range(C):
            if dfs(r, c, 0):
                print("YES")
                return

    print("NO")

if __name__ == "__main__":
    main()
