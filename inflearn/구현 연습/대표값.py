"""
n명의 학생들의 점수가 주어진다
이 점수들을 평균낸다(소수점 첫째자리 반올림)
평균과 가장 가까운 점수를 가진 학생은 몇 번째 학생인지 구하라

단 첫 번째 학생의 숫자는 1이다
답이 2개일 경우, 성적이 높은 학생의 번호를 출력한다
정답이 되는 점수가 같은 학생이 여럿일 경우 번호가 빠른 학생을 출력한다
"""

from operator import itemgetter

def print_number_of_student(arr, n):
    avg = sum(arr) / n
    avg = round(avg)
    minGap = float('inf')
    n = [] # minGap에 해당하는 학생들 번호, 점수를 저장
    for i in range(n):
        gap = abs(arr[i] - avg)
        if gap < minGap:
            minGap = gap
            n = [(i, arr[i])]
        elif gap == minGap:
            n.append((i, arr[i]))
    if len(n) == 1:
        return n[0][0] + 1 
    else:
        n.sort(key=itemgetter(0), reverse=True)
        n.sort(key=itemgetter(1), reverse=False)
        return n[0][0] + 1

        
####### 

ave = round(sum(arr) / n) 
min = float('inf')
for idx, x in enumerate(arr):
    dis = abs(x - ave)
    if dis < min:
        min = dis
        score = x
        num = idx + 1
    elif dis == min:
        if x > score:
            score = x
            num = idx + 1

print(ave, num)
        

"""
1. 정답인 사람이 여러명일 때 index가 빠른 사람을 고르라고 했는데, 이걸 별도 조건으로 체크할 필요가 없었다는 점 -> 왜냐면 for문은 앞에서 뒤로 도니까
2. 어차피 정답은 하나이므로, 굳이 배열에 저장해서 소팅할 게 아니라 돌면서 한 변수를 재활용하는 게 더 낫다는 점
"""
    


