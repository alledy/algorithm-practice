import heapq

def minheap(arr):
    h = []
    for x in arr:
        if x > 0:
            heapq.heappush(h,x)
        elif x == 0:
            print(heapq.heappop(h))
        else:
            return
    
minheap([5,3,6,0,5,0,2,4,0,-1])