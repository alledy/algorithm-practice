user_input = input()
n = int(user_input)

# 메모이제이션용 2차원 (n+1)*(n+1) 리스트 초기화하는 경우
# 나올 수 없는 값인 -1로 초기화한다.
# memo = []
# for i in range(n+1):
#     line = []
#     for j in range(n+1):
#         line.append(-1)
#     memo.append(line)

# 딕셔너리로 만들기
memo = {}

# 숫자 n을 k개의 무더기로 나누는 경우의 수


def p(memo, n, k):
    if (n, k) in memo:
        return memo[(n, k)]

    if k > n:
        memo[(n, k)] = 0
        return 0

    if k == 1:
        memo[(n, k)] = 1
        return 1

    if k == 2:
        memo[(n, k)] = n // 2
        return n // 2

    if k == n:
        memo[(n, k)] = 1
        return 1

    memo[(n, k)] = p(memo, n-1, k-1) + p(memo, n-k, k)
    return memo[(n, k)]


def solution(n):
    count = 0
    for i in range(1, n+1):
        count += p(memo, n, i)
    return count


print(solution(n))

# 또 다른 p(n,k)
# def p(n, k):
# 	count = 0
# 	if k > n:
# 		return 0
# 	if k == 1:
# 		return 1
# 	if k == 2:
# 		return n // 2
# 	if k == n:
# 		return 1

# 	for i in range(1, k+1):
# 		count += p(n-k, i)
# 	return count
