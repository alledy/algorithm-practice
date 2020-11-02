import heapq

def maxheap(arr):
    h = []
    for x in arr:
        if x > 0:
            heapq.heappush(h, -x)
        elif x == 0:
            print(-heapq.heappop(h))
        else:
            return