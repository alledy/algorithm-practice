# m은 필수이수과목 str
# arr은 수업설계 str[]

from collections import deque
def judge(q, s):
    for x in s:
        if x == q[0]:
            q.popleft()
        if len(q) == 0:
            return "YES"
    if len(q) > 0:
        return "NO"
    

def curriculum(m, arr):
    for string in arr:
        print(judge(deque(list(m)), string), end=' ')