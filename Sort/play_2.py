import random
from utils import switch


def is_right(func):
    def right(lists):
        # 生成List元素
        list_test = []

        for i in range(5):
            s = random.randint(100)
            list_test.append(i)
        result = func(list_test)
        return result

    return right


@is_right
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


sort_list = [3, 4, 1, 2, 5, 6, 8, 0]

sort_list = bubble_sort(sort_list)

print(sort_list)
