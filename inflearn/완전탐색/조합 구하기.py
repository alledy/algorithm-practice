"""
문제
1부터 N까지 번호가 적힌 구슬이 있을 때 이 중 M개를 뽑는 방법의 수를 출력
"""


n,m=4,2
# arr = [1,2,3,4]
# 이거 for문으로 돌릴 수 있나? (m이 무슨 값인지 모르는 상태에서?)

def combination_recursive(picked,d,pool):
    if d == m:
        print(picked)
        return 
    for i in range(len(pool)):
        picked.append(pool[i])
        rest = []
        for j in range(len(pool)):
            # 순열이랑 다른 점에 착안
            if i != j and picked[-1] < pool[j]: 
                rest.append(pool[j])
        combination_recursive(picked,d+1,rest)
        picked.pop()

# 더 효율적인 방법이 있을 것 같다

n,m=4,2
# 여기서 picked는 길이가 고정됨
arr = [x for x in range(1,n+1)]
def combination_recursive2(picked,d,ch):
    if d == m:
        print(picked)
        return
    for i in range(n):
        if ch[i] != 1 and (d == 0 or picked[d-1] < arr[i]):
            picked[d] = arr[i]
            ch[i] = 1
            combination_recursive2(picked,d+1,ch)
            ch[i] = 0

combination_recursive2([0 for x in range(m)], 0, [0 for x in range(n+1)])
# ch는 n을 기준으로, picked는 m을 기준으로 만들어져야 함

###### 개선해보자 ######
# for문을 돌 때, 내가 직전에 뽑은 원소 바로 뒤부터 for문을 돌아야 된다.
# 그러니까 위에서는 for문의 기준이 n으로 고정이었는데, 이게 고정이면 안된다는 소리. 
# 이 조건을 if문으로 추가하는 것보다 for 기준을 변동하는게 더 효과적
def combination_recursive_better(picked,d):
    if d == m:
        print(picked)
        return
    smallest = picked[d-1] if d > 0 else 0
    for x in range(smallest+1,n+1):
        picked[d] = x
        combination_recursive_better(picked,d+1)


