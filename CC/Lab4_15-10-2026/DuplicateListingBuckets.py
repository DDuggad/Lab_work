import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    titles = data[1:1 + n]

    groups = {}
    for title in titles:
        key = "".join(sorted(title))
        if key not in groups:
            groups[key] = []
        groups[key].append(title)

    print(len(groups))
    for group in groups.values():
        print(*group)

if __name__ == "__main__":
    main()
