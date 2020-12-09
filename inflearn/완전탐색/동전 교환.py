"""
문제:
목표 값이 있고, 원소들이 주어질 때, 더해서 목표값을 도출할 수 있는 최소한의 원소 개수를 구하여라
e.g. 목표값 15, 원소들 [1,2,5] => 5를 3개 쓰는게 제일 적게 원소를 사용하는 것.
"""

"""
바둑이 승차 문제랑 다른 점은, 최대가 아닌 최소를 구한다는 점. 
그리고 바둑이 승차 문제는 원소가 딱 한번만 사용될 수 있었기에 사용한다, 안한다의 2개의 선택만 있었는데
여기서는 하나의 원소를 여러번 쓰거나 안쓸 수 있다는 것.
즉 바둑이 승차 문제는 depth가 해당 원소 하나 하나 였음.
"""

"""
동전을 한 개 사용할 떄 -> 가지수 뻗기
동전을 두 개 사용할 때 -> 거기서 또 그 만큼의 가지수 뻗기를 반복
즉 depth가 동전의 개수인 셈
목표 값이 나오면 stop
"""

# arr 원소들
# v 목표값

v = 15
arr = [1,2,5]
m = float('inf')
def coin_exchange(s,d):    
    # d - depth
    # m - minimum count
    # s - sum
    global m
    if s > v:
        return
    if s == v:
        if d < m:
            m = d
        return
    for x in arr:
        n = s + x
        coin_exchange(n,d+1)
        
                    
coin_exchange(0,0)
print(m)