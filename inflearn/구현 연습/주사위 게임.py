"""
문제
주사위 3개를 던졌을 때 다음과 같은 규칙에 따라 상금을 받는다. 
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
N명이 주사위 게임에 참여했을 때, 가장 많이 상금을 받는 사람의 상금을 출력
"""

def calc(arr):
    # arr includes 3 number
    # 모든 숫자가 같을 때
    if arr[0] == arr[1] and arr[1] == arr[2]:
        return 10000 + arr[0] * 1000
    # 모든 숫자가 다를 때
    if arr[0] != arr[1] and arr[1] != arr[2] and arr[0] != arr[2]:
        return max(arr) * 100
    if arr[0] == arr[1] or arr[0] == arr[2]:
        return 1000 + arr[0] * 100
    return 1000 + arr[1] * 100


def solution(arr):
    # arr is 2 dimentional array
    max = 0
    for x in arr:
        if calc(x) > max:
            max = calc(x)
    return max 
    
