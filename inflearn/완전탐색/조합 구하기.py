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