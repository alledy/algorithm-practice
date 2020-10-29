# m은 필수이수과목 str
# arr은 수업설계 str[]

from collections import deque
def judge(m, s):
    for x in s:
        if x == m[0]:
            m = m[1:]
        if len(m) == 0:
            return "YES"
    if len(m) > 0:
        return "NO"
    

def curriculum(m, arr):
    for string in arr:
        print(judge(m, string), end=' ')