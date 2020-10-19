"""
문제
오름차순으로 정렬된 원소 N개 리스트, 원소 M개 리스트가 주어질 때,
두 리스트를 오름차순으로 합쳐 출력하시오
""" 

def solution(listA, listB):
    a,b=0,0
    answer = []
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            answer.append(listA[a])
            a += 1
        elif listA[a] > listB[b]:
            answer.append(listB[b])
            b += 1
        else:
            answer.extend([listA[a], listB[b]])
            a += 1
            b += 1
    if a == len(listA):
        answer += listB[b:]
    if b == len(listB):
        answer += listA[a:] 
    return answer 

            
            
