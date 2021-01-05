"""
문제: 지폐의 금액: T, 동전의 가지 수 k, 각 동전 하나의 금액 Pi와 개수 Ni가 주어질 때, 지폐를 동전으로 교환하는 방법의 가지 수를 출력하시오. 방법의 수는 2의 31승을 초과하지 않는다 가정한다.
입력 예시: 지폐 금액 20, [동전의 가치, 동전의 개수]가 k개 있는 이차원 배열 arr 
"""

t=20
k=3
arr=[[5,3],[10,2],[1,5]]

ans = 0

def exchange_coin2(d,s):
    global ans
    if s > t:
        return
    if d == k:
        if s == t:
            ans += 1
        return
    for i in range(arr[d][1]+1):
        exchange_coin2(d+1,s+i*arr[d][0])

exchange_coin2(0,0)
print(ans)
