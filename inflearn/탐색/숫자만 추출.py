"""
문제
문자와 숫자가 섞인 문자열 중 숫자만 추출하여 그 순서대로 자연수를 만든다
그 자연수와 자연수의 약수 개수를 출력한다
앞에 0이 붙을 경우 무시한다
""" 

def count_yaksu(n):
    count = 0
    r = n ** 0.5
    for i in range(1, int(r)+1):
        if n % i == 0:
            count += 1
    if r == int(r):
        return count * 2 - 1
    return count * 2
    

def solution(s):
    n = ''
    for i in s:
        if i.isdigit():
            n += i
    n = int(n)
    print(n, count_yaksu(n))
