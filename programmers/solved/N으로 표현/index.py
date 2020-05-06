def getMemo(N, n, number, memo):
    answer = set()
    for i in range(1, n):
        for x in memo[i]:
            for y in memo[n-i]:
                answer.add(x + y)
                answer.add(x - y)
                answer.add(x * y)
                if y != 0:
                    answer.add(x // y)
    answer.add(int(str(N)*n))
    return answer


def solution(N, number):
    memo = [set() for x in range(9)]
    if N == number:
        return 1
    else:
        memo[1].add(N)
    for n in range(2, 9):
        memo[n] = getMemo(N, n, number, memo)
        if number in memo[n]:
            return n
    return -1
