import sys
from collections import deque

def solve(k, s):
    n = len(s)
    active_ends = deque()
    current_flips = 0
    total_flips = 0

    for i in range(n):
        # Remove flips that no longer cover index i
        while active_ends and active_ends[0] == i:
            active_ends.popleft()
            current_flips -= 1

        # Calculate effective state at index i
        eff_state = (int(s[i]) + current_flips) % 2

        # If switch is OFF, we must initiate a flip starting at index i
        if eff_state == 0:
            if i + k > n:
                return -1
            total_flips += 1
            current_flips += 1
            active_ends.append(i + k)

    return total_flips

def main():
    d = sys.stdin.read().split()
    if not d:
        return

    t = int(d[0])
    results = []
    idx = 1
    for _ in range(t):
        k = int(d[idx])
        s = d[idx + 1]
        results.append(str(solve(k, s)))
        idx += 2

    print("\n".join(results))

if __name__ == "__main__":
    main()
