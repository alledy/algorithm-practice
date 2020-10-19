import sys
sys.stdin = open('input.txt', 'rt')
n, k = map(int, input().split()) # 가로로 2개의 숫자가 한 간격 띄고 나열된 경우

"""
문제: 자연수 n과 k가 주어졌을 때 n의 약수들 중 k번째로 작은 수를 출력하시오
없는 경우 -1 출력
"""

cnt = 0 
for i in range(1, n+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
    break
else:
    print(-1)

    
"""
for else 구문
for 문이 다 돌고 나서 break하지 않으면 else 구문으로 들어감
"""