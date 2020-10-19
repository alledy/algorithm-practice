"""
문제: N개의 자연수가 입력되면 각 자연수를 뒤집은 후, 그 뒤집은 수가 소수이면 그 수를 출력하라
"""


def isPrime(n):
    answer = True
    r = int(n ** 0.5)
    for i in range(2, r+1):
        if n % i == 0:
            answer = False
            break
    return answer
    

def reverse(n):
    n = str(n)[::-1]
    return int(n)

def solution(arr):
    for x in arr:
        r = reverse(x)
        if isPrime(r):
            print(r, end=' ')

#### 

def reverse2(n):
    ans = 0
    while n > 0:
        t = n % 10
        ans = ans * 10 + t
        n = n // 10
    return ans
    
"""
isPrime이 1이 들어올 가능성 추가해야함
"""
