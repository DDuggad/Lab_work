import sys

def max_supplies(costs, credits):
    costs.sort()
    count = 0
    for c in costs:
        if credits >= c:
            credits -= c
            count += 1
        else:
            break
    return count

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    costs = data[1:1 + n]
    credits = data[1 + n]
    print(max_supplies(costs, credits))

if __name__ == "__main__":
    main()
