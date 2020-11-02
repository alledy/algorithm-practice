from queue import Queue
# n은 총 왕자
# k는 k번째 수를 외치면 탈락하는 수
def save_princess(n,k):
    q = Queue()
    for i in range(1,n+1):
        q.put(i)
    goalCnt = k * (n-1)
    cnt = 0
    while q.qsize() > 1:
        cnt += 1
        if cnt % k == 0:
            q.get()
        else:
            q.put(q.get())
    return q.get()

        
        
"""
deque로도 할 수 있다. 
deque의 popleft와 append를 사용하면 된다. 
"""
        
    

