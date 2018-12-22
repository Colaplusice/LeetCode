import random


def heapsort(num):
    """
    堆排序
    :param num:
    :return: list
    先构建最大堆
    Build_max_heap
    每次取出最大的元素，然后进行调整堆
    Max_heapify
    每个节点的 左节点等于这个节点的值*2+1
    每个节点的 右节点等于这个节点的值*2+2
    """


def Max_heapify(heap, Heapsize, root):
    left = root * 2 + 1
    right = root * 2 + 2
    # lager=root
    # left child
    if left < Heapsize and heap[left] > heap[root]:
        heap[left], heap[root] = heap[root], heap[left]
        Max_heapify(heap, Heapsize, left)
    if right < Heapsize and heap[right] > heap[root]:
        heap[right], heap[root] = heap[root], heap[right]
        Max_heapify(heap, Heapsize, right)


# 还要增加一步


# 构建堆
def build_maxHeap(heap):
    Heapsize = len(heap)
    # 依次找到所有的根节点
    for i in range((Heapsize - 2) // 2, -1, -1):
        Max_heapify(heap, Heapsize, i)
    print("this is heap")
    print(heap)
    # print(lists[i])


def HeapSort(heap):
    # 建立最大堆
    build_maxHeap(heap)
    for i in range(len(heap) - 1, -1, -1):
        print(i)
        heap[i], heap[0] = heap[0], heap[i]
        # 最大堆化
        Max_heapify(heap, i, 0)
    print(heap)


if __name__ == "__main__":
    ## 调整好的lists

    lists = [10, 9, 7, 8, 5, 6, 3, 1, 4, 2]
    shuff_list = [8, 9, 10, 6, 3, 4, 5, 7, 1, 2]

    print(lists)
    # random.shuffle(lists)
    HeapSort(shuff_list)
