def solution(arr, n, m):
    # arr의 길이는 n
    i = 0
    while i < m:
        [mi, ma]=find_min_max(arr)
        arr[mi[0]] = mi[1] + 1
        arr[ma[0]] = ma[1] - 1
        i += 1
    [mi,ma] = find_min_max(arr)
    return ma[1] - mi[1]

def find_min_max(arr):
    mi, ma = 100,0
    mii, mai = 0,0
    for i,x in enumerate(arr):
        if x > ma:
            ma = x
            mai = i
        if x < mi:
            mi = x
            mii = i
    return [(mii, mi), (mai, ma)]
    