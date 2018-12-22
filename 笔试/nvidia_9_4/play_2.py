nums = 0


def Max_heapify(heap, Heapsize, root):
    print(root)
    global nums
    left = root * 2 + 1
    right = root * 2 + 2
    # lager=root
    # left child
    if left < Heapsize and heap[left] > heap[root]:
        heap[left], heap[root] = heap[root], heap[left]
        nums += 1
        Max_heapify(heap, Heapsize, left)
    if right < Heapsize and heap[right] < heap[root]:
        nums += 1
        heap[right], heap[root] = heap[root], heap[right]
        Max_heapify(heap, Heapsize, right)


# 还要增加一步


# 构建堆
def build_maxHeap(heap):
    Heapsize = len(heap)
    print(heap)
    # 依次找到所有的根节点
    for i in range((Heapsize - 2) // 2, -1, -1):
        Max_heapify(heap, Heapsize, i)
    print("this is heap")
    print(nums)
    print(heap)
    # print(lists[i])


heap = [10, 9, 7, 8, 5, 6, 3, 1, 4, 2]

build_maxHeap(heap)
