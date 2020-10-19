
def isPeak(narr, ix, iy):
    t = narr[ix][iy]
    if t > narr[ix-1][iy] and t > narr[ix+1][iy] and t> narr[ix][iy-1] and t > narr[ix][iy+1]:
        return True
    return False



def solution(arr, n):
    # arr는 2차원 배열 n*n 사이즈
    not_peak = []
    # 인덱스 x,y가 하나가 0이거나 n-1일 경우에는 index out of range를 주의해야 한다 -> 그냥 주변이 0으로 둘러싸인 새로운 배열을 만들자
    narr = [[0] * (n+2) for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            narr[i][j] = arr[i-1][j-1]
    
    # 원래 배열의 크기 만큼 2중 포문 돌려서 isPeak인지 확인하고 카운트 세기
    answer = 0
    for i in range(1,n+1):
        for j in range(n+1):
            if isPeak(narr, i, j): 
                answer += 1
    return answer


arr = [[5,3,7,2,3], [3,7,1,6,1], [7,2,5,3,4], [4,3,6,4,1], [8,7,3,5,2]]
solution(arr,5)

def solution2(arr, n):
    # arr 둘레에 0 붙이기
    arr.insert(0, [0]*n)
    arr.append([0]*n)
    for x in arr:
        x.insert(0,0)
        x.append(0)
    
    # 이중 포문을 돌면서, 해당 원소가 봉우리인지 체크하는데, all을 사용한다
    count = 0 
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if all(arr[i][j] > arr[i+dx[k]][j+dy[k]] for k in range(4)):
                count += 1
    return count