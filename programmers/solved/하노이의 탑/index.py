# f: 시작점
# t: 도착점
# b: 중간점

# a에서 b로 이동하는 함수


def move(a, b):
    return [a, b]

# n개를 f에서 t로 옮기는 경로 2차원 배열


def path(n, f, b, t):
    if n == 1:
        return [move(f, t)]
    answer = path(n-1, f, t, b) + [move(f, t)] + path(n-1, b, f, t)
    return answer


def solution(n):
    return path(n, 1, 2, 3)
