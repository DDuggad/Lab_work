import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n, m, c = data[0], data[1], data[2]
    arr = data[3:3 + n]
    bus = data[3 + n:3 + n + m]

    out = ["MISSED"] * n
    q = deque()

    student_idx = 0
    for dep_time in bus:
        while student_idx < n and arr[student_idx] <= dep_time:
            q.append(student_idx)
            student_idx += 1

        boarded = 0
        while q and boarded < c:
            s_i = q.popleft()
            out[s_i] = str(dep_time)
            boarded += 1

    print(*out)

if __name__ == "__main__":
    main()
