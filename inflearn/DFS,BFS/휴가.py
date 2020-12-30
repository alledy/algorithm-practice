"""
문제: 카운셀러에게 상담 스케줄이 주어진다. N일 동안 상담을 할 수 있다고 할 때, 해당 스케줄 내에서 최대로 얻을 수 있는 수익을 구하시오. 
입력: 1일부터 N일 간의 상담 스케줄. [상담에 걸리는 일수, 이익]을 원소로 하는 N 길이의 이차원 배열 arr. 
"""
n=7
arr=[[4,20],[2,10],[3,15],[3,20],[2,30],[2,20],[1,10]]
max_pay=0
def get_max_earn(d,pay):
    global max_pay
    if d > n:
        return
    if pay > max_pay:
        max_pay = pay
    # 선택 안하기로 한 경우
    get_max_earn(d+1,pay)
    # 선택하기로 한 경우
    if d < n:
        get_max_earn(d+arr[d][0],pay+arr[d][1])

get_max_earn(0,0)
print(max_pay)
