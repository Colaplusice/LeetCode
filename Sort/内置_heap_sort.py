from heapq import heappush,heappop

def heapsort(iterable):

    h=[]
    for value in iterable:
        heappush(h,iterable)
    return [heappop(h) for i in range(len(h))]



heapsort()