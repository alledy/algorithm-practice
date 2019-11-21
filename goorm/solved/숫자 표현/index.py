user_input = input()
n = int(user_input)

# 숫자 n을 k개의 무더기로 나누는 경우의 수


def p(n, k):
    if k > n:
        return 0
    if k == 1:
        return 1
    if k == 2:
        return n // 2
    if k == n:
        return 1
    return p(n-1, k-1) + p(n-k, k)


def solution(n):
    count = 0
    for i in range(1, n+1):
        count += p(n, i)
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
