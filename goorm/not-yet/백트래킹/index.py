# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
str_list = input().split()

# int형으로 저장
length = int(user_input)

n_list = []
for i in str_list:
    n_list.append(int(i))


def backtracking(length, n_list):
    # 계산값과 뎁스를 튜플 형태로 저장
    start_node = (n_list[0], 0)
    stack = [start_node]
    count = 0

    while stack:
        node = stack.pop()
        calc_res = node[0]
        depth = node[1]

        # 마지막 뎁스인지 아닌지 체크
        # 마지막 뎁스일 때 계산값이 리스트 마지막 원소값와 일치하는지 체크
        # continue indent 주의
        if depth == length-2:
            if calc_res == n_list[-1]:
                count += 1
            continue

        # 마지막 뎁스가 아닐 경우 다음 값을 가져옴
        next_num = n_list[depth+1]

        # 0이상 20이하 조건 체크 후 스택에 푸시
        # + 일 때
        plus_calc_res = calc_res + next_num
        if (plus_calc_res >= 0) and (plus_calc_res <= 20):
            stack.append((plus_calc_res, depth+1))

        # - 일 때
        sub_calc_res = calc_res - next_num
        if (sub_calc_res >= 0) and (sub_calc_res <= 20):
            stack.append((sub_calc_res, depth+1))

    return count


print(backtracking(length, n_list))
