import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    r = data[1:1 + n]

    pickup = [0] * n
    max_ready = 0
    max_wait = -1
    best_token = -1

    for i in range(n):
        ready = r[i]
        if ready > max_ready:
            max_ready = ready
        pickup[i] = max_ready
        wait = max_ready - ready
        if wait > max_wait:
            max_wait = wait
            best_token = i + 1

    print(*pickup)
    print(f"{max_wait} {best_token}")

if __name__ == "__main__":
    main()
