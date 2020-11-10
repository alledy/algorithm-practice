# N개의 원소로 구성된 자연수 집합이 주어지면 (n <= 10, 원소는 중복되지 않는다)
# 이 집합을 두 개의 부분집합으로 나누었을 때 
# 두 부분집합의 원소 합이 서로 같은 경우가 존재하면 YES, 아니면 NO
def same_sum(x,y):
    if sum(x) == sum(y):
        return True
    return False

def judge_same_sum(arr, checked):
    x = []
    y = []
    for i, v in enumerate(checked):
        if v == 1:
            x.append(arr[i])
        else:
            y.append(arr[i])
    return same_sum(x,y)
            
def same_sum_subset(arr, checked, depth):
    # print(checked, depth)
    # arr은 자연수 집합
    if depth == len(arr):
        res = judge_same_sum(arr, checked)
        if res:
            return "YES"
        return "NO"
    # 하나를 처리
    checked[depth] = 0
    same_sum_subset(arr, checked, depth+1)
    checked[depth] = 1
    same_sum_subset(arr, checked, depth+1)
    
    
same_sum_subset([1,3,5,6,7,10], [0,0,0,0,0,0], 0)