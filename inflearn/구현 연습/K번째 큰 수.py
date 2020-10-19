"""
문제: n개의 숫자열(숫자는 1이상 100이하)이 주어질 때, 그 중 3개를 뽑아 합한다. 이를 모든 경우의 수에 대해 한다. 
그랬을 때 이 중 K번째로 큰 수를 출력하시오. 
"""

# nC3 
# 이거는 그냥 해봐야 되는거 아닌가?

# arr -> n개의 숫자가 담긴 리스트

result = []

for x in range(n):
    for y in range (x+1, n):
        for z in range(y+1, n):
            result.append(arr[x] + arr[y] + arr[z])
result.sort(reverse=True)
print(result[k-1])

###########

a = list(map(int, input().split()) 

res = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i] + a[j] + a[m])

res = list(res) 
res.sort(reverse=True)
print(res[k-1])

"""
set은 sort가 안된다는 점
set을 썼어야 k번째 수를 찾을 수 있다는 점
"""