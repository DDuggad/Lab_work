import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, count_left = merge_sort(arr[:mid])
    right, count_right = merge_sort(arr[mid:])

    merged = []
    i = j = 0
    inv = count_left + count_right

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:1 + n]]
    _, total_inversions = merge_sort(a)
    print(total_inversions)

if __name__ == "__main__":
    solve()
