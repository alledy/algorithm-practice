"""
문제: 1부터 n까지 숫자가 있을 때 그 중 m개를 뽑아 오름차순으로 정렬할 수 있는 경우를 모두 프린트 하시오. (출력순은 오름차순)
"""

"""
Thinking point🙉
permutation이라는 함수가 하는 일은 원소를 한 개 뽑고, 나머지 남은 원소(pickable)들 중 하나를 뽑는 것이다. 
그런데 그 한 개를 뽑을 가능한 경우의 수가 만약 n이 3이라면 1, 2, 3 즉 세가지 경우의 수가 나오게 된다.
즉 Depth가 한 번일 때, 가능한 경우의 수 만큼 처리를 하고 다음 depth로 넘거야 한다. (즉 for문을 써야한다는 얘기)
"""

n,m = 3,2

def permutation(pickable, picked):
    if len(pickable) == n-m: 
        print(picked)
        return
    else:
        for i in range(len(pickable)):
            picked.append(pickable[i])
            rest_pickable = []
            for j in range(len(pickable)):
                if i != j:
                    rest_pickable.append(pickable[j])
            permutation(rest_pickable, picked)
            picked.pop()

permutation([x for x in range(1, n+1)], [])