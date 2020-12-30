"""
문제: 제한시간 안에 문제를 푸는데, 각 문제를 푸는 데 걸리는 시간은 정해져있으며 각 문제마다 배점이 다르다. 해당 시간이 걸리면 문제는 푼 것으로 간주하고, 얻을 수 있는 최대 점수를 출력.
입력: 제한시간 M, 총 문제 N, [점수, 푸는데 걸리는 시간]으로 이루어진 2차원 배열 arr 
"""

# 완탐(조합)이랑 다른가?
n,m=5,20
arr=[[10,5],[25,12],[15,8],[6,3],[7,4]]
max_score=0
    
def get_best_score2(d,s,t):
    global max_score
    if t > m:
        return
    if d == n:    
        if s > max_score:
            max_score = s
        return
    # 선택안하기로 한 경우
    get_best_score2(d+1,s,t)
    # 선택하기로 한 경우
    get_best_score2(d+1,s+arr[d][0],t+arr[d][1])
     
get_best_score2(0,0,0)
print(max_score)