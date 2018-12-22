def bubble_sort(lists):
    if not lists:
        return
    for i in range(len(lists) - 1, -1, -1):
        for j in range(i):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists


base_array = []
a_list = input().split(" ")
for _ in range(len(a_list)):
    base_array.extend(input().strip().split(" "))

base_array = [int(a) for a in base_array]
base_array = bubble_sort(base_array)
print(" ".join([str(a) for a in base_array]))
