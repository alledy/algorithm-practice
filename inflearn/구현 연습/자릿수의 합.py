"""
문제
n개의 자연수가 입력되면, 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력하시오
"""

def digit_sum(n):
    arr = str(n).split()
    sum = 0
    for x in arr:
        sum += int(x)
    return sum
    
def solution(arr):
    m = 0
    for x in arr:
        if digit_sum(m) < digit_sum(x):
            m = x
    return m

#### Wrong Above! #####

def digit_sum2(n):
    arr = list(str(n))
    sum = 0
    for x in arr:
        sum += int(x)
    return sum
    
def solution2(arr):
    ms, answer = 0,0
    for x in arr:
        s = digit_sum(x)
        if ms < s:
            ms = s
            answer = x 
    return answer 

"""
한글자씩 스트링 쪼갤 때 그냥 list로 감싸면 됐었다
split() 이건 스페이스 기준으로 자르는거
"""
       
### 타입 변환하지 않고 하기 
def digit_sum3(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum 