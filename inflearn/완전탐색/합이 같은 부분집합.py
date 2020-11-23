
import sys
# N개의 원소로 구성된 자연수 집합이 주어지면 (n <= 10, 원소는 중복되지 않는다)
# 이 집합을 두 개의 부분집합으로 나누었을 때 
# 두 부분집합의 원소 합이 서로 같은 경우가 존재하면 YES, 아니면 NO
def same_sum(x,y):
    if sum(x) == sum(y):
        return True
    return False

def judge_same_sum(arr, checked):
    x,y=[],[]
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
            print("YES")
            sys.exit()
    # 하나를 처리
    checked[depth] = 0
    same_sum_subset(arr, checked, depth+1)
    checked[depth] = 1
    same_sum_subset(arr, checked, depth+1)

def main(arr):
    same_sum_subset(arr, [0,0,0,0,0,0], 0)
    print("NO")

########## 부분집합 sum을 구하는 더 나은 방법 ##########
# 일단 전체 arr sum의 절반 이상이 넘으면 더 이상 계산할 필요가 없다
# checked라는 번거로운 아이를 넘겨서 계산할 때 또 다른 함수를 부르는 것보다 
# 그냥 부분집합의 합 자체를 넘기는 것이 효율적

def same_sum_subset2(arr, s, d):
    half = sum(arr)/2
    if s > half:
        return
    if d == len(arr):
        if s == half:
            print("YES")
            sys.exit()
        return
    same_sum_subset2(arr, s, d+1)
    s += arr[d]
    same_sum_subset2(arr, s, d+1)

def main2(arr):
    same_sum_subset2(arr, 0, 0)
    print("NO")
    