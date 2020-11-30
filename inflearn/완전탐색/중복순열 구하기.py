"""
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
"""

# picked는 고른 숫자들이 담겨 있는 배열
# to_pick은 남은 개수
def multiset_permutation(picked, to_pick, n):
    if to_pick == 0:
        print(picked)
        return
    for i in range(1, n+1):
        picked.append(i)
        multiset_permutation(picked, to_pick-1, n) 
        picked.pop()
    
