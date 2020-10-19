"""
문제
OX문제의 결과가 주어질 때 총 점수를 계산하시오

1번 문제가 맞는 경우에는 1점으로 계산한다. 
앞의 문제에 대해서는 답을 틀리다가 답이 맞는 처음 문제는 1점으로 계산한다. 
또한, 연속으로 문제의 답이 맞는 경우에서 두 번째 문제는 2점, 세 번째 문제는 3점, ..., K번째 문제는 K점으로 계산한다. 
틀린 문제는 0점으로 계 산한다.
"""

def solution(n, arr):
    # arr includes ox result in order
    # n is length of arr (number of ox quiz)
    answer, idx, success = 0,0,0
    while idx < n:
        if arr[idx] == 1:
            answer += success + 1 
            success += 1
        else:
            success = 0
        idx += 1 
    return answer 


