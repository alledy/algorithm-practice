"""
문제
구간이 주어지면, 해당 구간의 카드를 거꾸로 뒤집어라. 
단 첫번째 카드는 숫자 1부터 표기한다. 
10번 이 작업을 수행했을 때 마지막 카드 배치를 출력하라.
"""

import sys
sys.stdin = open('input.txt', 'rt') 


def reverse_arr(arr, s, e):
    return reversed(arr[s:e+1])

def solution():
    arr = [0] * 21
    for i in range(arr):
        arr[i] = i # 더 쉽게 초기화 가능? 
    for _ in range(10):
        s, e = map(int, input().split())
        arr = reverse_arr(arr, s, e)
    return arr[1:]



