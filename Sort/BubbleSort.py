from  utils import switch

def bubble_sort(lists):
    # 数组的长度
    length = len(lists)

    # 数组的length-1
    for i in reversed(range(length)):
        # 1数组的length-2 因为要和Index+1来比较
        for j in range(i):
            if lists[j] > lists[j + 1]:
                switch(lists, j, j + 1)

    return lists



a=[1,2,34,5,7,88,8,8,8,8]

lists=bubble_sort(a)
print(lists)
