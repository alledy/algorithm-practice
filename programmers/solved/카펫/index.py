# yellow가 n*m이면, brown은 2(n+m+2), 전체는 (n+2)*(m+2)
# n >= m

def solution(brown, yellow):
    for m in range(1, int(yellow ** 0.5) + 1):
        if yellow % m == 0 and (yellow // m + m + 2) * 2 == brown:
            return [yellow // m + 2, m + 2]