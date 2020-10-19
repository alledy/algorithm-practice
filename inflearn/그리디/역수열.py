"""
역수열이 주어졌을 때 원래 수열을 출력
"""

# arr은 역수열
# 원래 수열 리턴해야함
def yuk_su(arr):
    ans = [0] * len(arr)

    for cur_n in range(1, len(arr)+1):
        target = arr[cur_n-1]
        cnt = 0
        for p, x in enumerate(ans):
            if target == cnt:
                if x == 0:
                    ans[p] = cur_n
                    break
                else:
                    continue
            if x == 0:
                cnt += 1
                        
    return ans

yuk_su([5,3,4,0,2,1,1,0])
