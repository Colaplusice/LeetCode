def bubble_sort(lists):
    length = len(lists)
    for i in reversed(range(length)):
        for j in range(i):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]

    return lists


a = [1, 2, 34, 5, 7, 88, 8, 8, 8, 8]

lists = bubble_sort(a)
print(lists)
