"""
문제: 자연수 N이 주어질 때 1부터 N까지의 소수 개수를 출력하는 프로그램을 작성하세요
"""

def isPrime(n):
    answer = True
    r = int(n ** 0.5)
    for i in range(2, r+1):
        if n % i == 0:
            answer = False
            break
    return answer
    

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if isPrime(i):
            answer += 1
    return answer


### 에라토스테네스 체 ### 

def solution2(n):
    arr = [0] * (n+1)
    answer = 0
    for i in range(2, n+1):
        if arr[i] == 0:
            answer += 1 
            for j in range(i+i, n+1, i):
                arr[j] = 1
    return answer

