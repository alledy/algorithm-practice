def calc(sa, l, c):
    cnt,idx = 1,1
    tmp = sa[0]

    while idx < len(sa):
        if tmp+l <= sa[idx]:
            cnt += 1
            tmp = sa[idx]  
            if cnt == c:
                break
        idx += 1
    return cnt
            
    
def solution(arr, n, c):
    # arr은 정렬되지 않은 좌표
    # c는 배치해야 하는 말의 개수
    ans = 0
    sa = sorted(arr)
    s, e = sa[0], sa[-1]
    while s <= e:
        l = (s+e)//2
        if calc(sa,l,c) == c:
            ans = l
            s = l+1
        else:
            e = l-1
    return ans
                    
solution([1,2,8,4,9],5,3)