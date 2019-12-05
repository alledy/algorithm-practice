total_n = int(input())
str_list = input().split(' ')
n_list = [int(i) for i in str_list]

# 맨 앞과 맨 뒤에 추가된 0은 시작점과 착지점
my_list = [0] + n_list + [0]
memo = {}


def p(list):
    memo[0] = list[0]
    memo[1] = list[1]
    memo[2] = list[2]
    memo[3] = list[3]

    for index in range(4, len(list)):
        memo[index] = min(memo[index-1], memo[index-2],
                          memo[index-3]) + list[index]
    return memo[len(list)-1]


print(p(my_list))
