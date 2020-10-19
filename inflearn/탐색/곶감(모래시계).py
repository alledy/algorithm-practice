"""
문제
n은 홀수, n*n 배열이 주어짐
회전 명령이 m번 주어짐
회전 명령은 a,b,c 로 이루어지는데 a번째 행(첫번째 행은 1행)을 b가 0이면 왼쪽으로 1이면 오른쪽으로, c만큼 이동하라는 뜻
"""

def calc_sum(n,arr):
    answer = 0
    s,e = 0, n-1
    for i in range(n):
        for j in range(s,e+1):
            answer += arr[i][j]
        if i < n//2:    
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1
    return answer

def solution(n, arr, order):
    # n은 2차원 배열 arr의 크기
    # m은 order의 길이
    # order는 3*m 배열 
    for x in order:
        a, b, c = x[0], x[1], x[2]
        new_arr = [0] * n
        move = n - c if b == 0 else c
        for i in range(n):
            new_i =  i + move - n if i + move >= n else i + move
            new_arr[new_i] = arr[a-1][i]
        arr[a-1] = new_arr    
    return calc_sum(n,arr) 
         
"""
2차원 배열... 1차원과 섞어쓸 때 뎁스가..
"""     

"""
새로운 arr를 만들어서 교체했었는데, 
인덱스를 갖고 움직이지 말고, 한칸씩 이동하는 거니까, append와 insert와 pop을 갖고 하면 하나씩 이동할 수 있다. 
e.g. arr.append(arr.pop(0)) => 앞에 원소를 뺀다음, 뒤에 삽입. 왼쪽으로 한칸 이동
e.g. arr.insert(0, arr.pop()) => 뒤의 원소를 뺀다음 앞에 삽입. 오른쪽 한칸 이동
"""