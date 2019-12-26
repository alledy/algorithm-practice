user_input = input().split(' ')
# total days
n = int(user_input[0])
# total ranges
m = int(user_input[1])

# 인덱스 맞추기 위해 앞에 원소 삽입
account = input().split(' ')
account = [0] + [int(i) for i in account]

memo = {}


def print_account(acc, m):
    for i in range(m):
        str_list = input().split(' ')
        start = int(str_list[0])
        end = int(str_list[1])

        answer = calc(memo, start, end, acc)

        if answer > 0:
            print('+'+str(answer))
        else:
            print(answer)


def calc(memo, start, end, acc):
    if (start, end) in memo:
        return memo[(start, end)]

    if start == end:
        memo[(start, end)] = acc[start]
        return memo[(start, end)]

    memo[(start, end)] = calc(memo, start, end-1, acc) + acc[end]
    return memo[(start, end)]


print_account(account, m)
