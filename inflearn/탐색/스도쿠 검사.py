# 1. 각 행에 겹치는 문자가 없는지
# 2. 각 열에 겹치는 문자가 없는지
# 3. 3*3에 겹치는 문자가 없는지

def solution(arr):
    # arr 9*9
    # set에 넣고.. 
    # 근데 이걸 일일이 하면 되게 비효율적일 것 같긴 한데 일단 해본다
    s, ss = set(), set()
    for i in range(9):
        for j in range(9):
            s.add(arr[i][j])
            ss.add([arr[j][i]])
        if len(s) != 9 or len(ss) != 9:
            return "NO"
        s.clear()
        ss.clear()
    
    
"""
여기서 3*3 그룹 탐색하는게 제일 까다로움 
4중 포문 돌려야 함
처음 2개는 어떤 그룹을 탐색할 건지 정하는 거고,
그 다음 2개는 선택된 그룹 안에서 한개씩 탐색하는 거임
"""

def solution2(arr):
    # checklist 1 - 행 
    # checklist 2 - 열
    # checklist 3 - 그룹
    # checklist는 원소가 10개인 배열이고, 탐색한 값을 인덱스라고 보고 1 처리함
    # sum이 9면 ok 
    # 중복된 게 있으면 sum이 9가 안나옴
    
    for i in range(arr):
        ch1, ch2 = [0]*10, [0]*10
        for j in range(arr):
            ch1[arr[i][j]] = 1
            ch2[arr[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    
    for a in range(3):
        for b in range(3):
            ch3 = [0]*10
            for c in range(3):
                for d in range(3):
                    ch3[arr[a*3+c][b*3+d]] = 1
            if sum(ch3) != 9:
                return False
    return True

    

