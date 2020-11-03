# 10진수 수가 주어지면 2진수 출력. 단 재귀를 통해서.

    
# def r(n):
#     if n >= 2:
#         r(n//2)
#         print(n%2)
#     else:
#         print(n)
# r(11)

def r(ans, n):
    if n < 2:
        ans.append(n)
        return ans
    else:
        ans.append(n%2)
        return r(ans, n//2)

def get_binary(n):
    ans = []
    l = r(ans, n)
    return sum([x*(10**i) for i, x in enumerate(l)])

get_binary(11)