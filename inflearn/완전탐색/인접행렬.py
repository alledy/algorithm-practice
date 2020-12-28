"""
문제: 가중치 방향 그래프가 주어졌을 때 인접행렬로 나타내라
입력: 정점의 수 n, 간선의 수 m, [정점1, 정점2, 거리] 배열 m개로 이루어진 이차원 배열 arr (e.g. [[1,2,7], [1,3,4]...])
""" 

# 일단 output은 n*n 행렬
# 값 0으로 만들어진 2차원 배열로 초기화하고
# arr 읽으면서 값 넣어주면 끝일듯?

def adjacency_matrix(n,m,arr):
    ans = [[0 for x in range(n)] for y in range(n)]
    for x in arr:
        [n1,n2,dis] = x
        ans[n1-1][n2-1] = dis
    return ans 
