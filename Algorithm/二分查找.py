def find(array, num):
    if len(array) == 1:
        if num == array[0]:
            return 0
        else:
            return -1
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] > num:
            high = mid - 1

        elif array[mid] < num:
            low = mid + 1
        else:
            return mid


array = [1, 2, 3, 4, 5, 6]

result = find(array, 6)
print(result)
