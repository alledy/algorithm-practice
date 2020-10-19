# 특정 범위 안에 답이 있다

def solution(arr, k, n):
    # k개 길이 arr
    # n만큼의 개수가 나오도록 하는 최대 길이 m 구하기
    # m의 범위 -> 1~arr의 최대값
    # arr의 최대값보다 크면 아예 만들 수가 없으니까 n은 0 나올 수밖에 없다
    # 그러나 n은 1 이상인 값이니까 

    # 답이 될 수 있는 것은 여러 가지인데 그중에서 제일 좋은 값, 제일 큰 값을 골라야 하는 것
    answer = 0
    s, e = 1, max(arr)
    while s <= e:
        count = 0
        m = (s+e)//2
        for x in arr:
            count += x//m
            if count >= n:
                answer = m
                s = m+1
                break
        else:
            e = m-1
    return answer
        

"""최선의 답을 고르는 문제"""