user_input = input().split(' ')
# total days
n = int(user_input[0])
# total ranges
m = int(user_input[1])

# 수입과 지출을 나타내는 리스트
account = input().split(' ')
account = [int(i) for i in account]


def calc(account, m):
    sum_from_start = [account[0]]

    for index in range(1, len(account)):
        total = sum_from_start[index-1] + account[index]
        sum_from_start.append(total)

    for i in range(m):
        str_list = input().split(' ')
        start = int(str_list[0])
        end = int(str_list[1])

        if start == end:
            print_calc(account[start-1])
        elif start == 1:
            print_calc(sum_from_start[end-1])
        else:
            pre_end = start-1
            print_calc(sum_from_start[end-1] - sum_from_start[pre_end-1])


def print_calc(n):
    if n > 0:
        print('+'+str(n))
    else:
        print(n)


calc(account, m)
