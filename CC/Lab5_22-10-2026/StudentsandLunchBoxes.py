import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    students = data[1:1 + n]
    boxes = data[1 + n:1 + 2 * n]

    count_0 = students.count('0')
    count_1 = students.count('1')

    for box in boxes:
        if box == '0':
            if count_0 > 0:
                count_0 -= 1
            else:
                break
        else:
            if count_1 > 0:
                count_1 -= 1
            else:
                break

    print(count_0 + count_1)

if __name__ == "__main__":
    main()
