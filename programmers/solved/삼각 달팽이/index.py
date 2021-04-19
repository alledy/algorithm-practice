# 방향은 총 3개가 반복됨
# x 증가 y 그대로
# x 그대로 y 증가
# x 그대로 y 그대로

# n, n - 1, n - 2, n - 3, .... 1 까지 
def solution(n):
    X, Y = 0, 1
    arr = [[0] * n for _ in range(n)] # n * n 길이 2차 배열
    count = n
    num = 1
    index = [0, 0]
    while count:
        for c in range(count):
            arr[index[X]][index[Y]] = num
            num += 1
            if abs(count - n) % 3 == 0:
                if c != count - 1:
                    index[X] += 1
                else:
                    index[Y] += 1
            elif abs(count - n) % 3 == 1:
                if c != count - 1:
                    index[Y] += 1
                else:
                    index[X] -= 1
                    index[Y] -= 1
            else:
                if c != count - 1:
                    index[X] -= 1
                    index[Y] -= 1
                else:
                    index[X] += 1
        count -= 1
    
    return [arr[i][j] for i in range(n) for j in range(n) if arr[i][j] != 0]