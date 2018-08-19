import random


def quickSort(array):
    if len(array) < 2:
        return array

    left = [i for i in array[1:] if i <= array[0]]

    right = [i for i in array[1:] if i > array[0]]

    return quickSort(left) + [array[0]] + quickSort(right)


sd = [3, 8, 11, 96, 48, 50, 50, 91, 65, 31]
result = quickSort(sd)

print(result)
