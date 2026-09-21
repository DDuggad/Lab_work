print("Enter elements: ")
arr = input().split()
val = input("Enter element to be searched: ")
i = -1
found = False
for a in arr:
    i += 1
    if a == val:
        print("Element found at index: ", i)
        found = True
        break
if not found:
    print("Element not found!")

val = int(input("Enter value to be searched: "))
arr = input("Enter elements (sorted): ").split()
n = len(arr)
min, max = 0, n - 1
found = False

while min <= max:
    mid = (min + max) // 2
    if int(arr[mid]) == val:
        print("Element found at index: ", mid)
        found = True
        break
    elif int(arr[mid]) > val:
        max = mid - 1
    else:
        min = mid + 1

if not found:
    print("Element not found!")
