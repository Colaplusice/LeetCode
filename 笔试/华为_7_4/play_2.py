def bubble_sort(alist):
    n = len(alist)
    for j in range(n - 1):
        count = 0
        for i in range(0, n - 1 - j):
            if alist[i][1] > alist[i + 1][1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
        if 0 == count:
            break
    return alist


a = input()
sd = a.split(",")

record_list = []
result_list = []
for index, each in enumerate(sd):
    record_list.append([index, ord(each[-1])])

record_list = bubble_sort(record_list)

result_list = [sd[i[0]] for i in record_list]
result_list.reverse()
print(",".join(result_list))
