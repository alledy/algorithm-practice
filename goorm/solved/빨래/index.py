user_input = input().split(' ')
total_col = int(user_input[0])  # e.g. 3 => 총 3가지 컬러
total_clothes = int(user_input[1])  # e.g. 5 => 총 5벌의 옷

color_input = input().split(' ')  # ['red', 'black', 'blue']
clothes_dic = {}
for i in color_input:
    clothes_dic[i] = []  # {'red': [], 'black': [], 'blue': []}

for i in range(total_clothes):
    cloth_info = input().split(' ')
    time = int(cloth_info[0])
    col = cloth_info[1]

    # {'red': [3,4], 'black': [2,5], 'blue': [5]}
    clothes_dic[col].append(time)


# 특정 컬러의 옷을 전부 세탁하는 데 걸리는 최소 시간
# 전부 합하면 됨
def total_wash_time(dic):
    answer = 0
    for c_list in dic.values():
        answer += min_wash_time(c_list)

    return answer

# 해당 컬러의 옷 세탁에 걸리는 시간을 원소로 가진 리스트(e.g. [5,5,5])


user_input = input().split(' ')
total_col = int(user_input[0])
total_clothes = int(user_input[1])

color_input = input().split(' ')
clothes_dic = {}
for i in color_input:
    clothes_dic[i] = []

for i in range(total_clothes):
    cloth_info = input().split(' ')
    time = int(cloth_info[0])
    col = cloth_info[1]

    clothes_dic[col].append(time)


# 특정 컬러의 옷을 전부 세탁하는 데 걸리는 최소 시간
# 전부 합하면 됨
def total_wash_time(dic):
    answer = 0
    for c_list in dic.values():
        answer += min_wash_time(c_list)

    return answer

# 해당 컬러의 옷 세탁에 걸리는 시간을 원소로 가진 리스트(e.g. [5,5,5])가 인자
# 같은 컬러의 옷을 2개씩 함께 빨래할 수 있다
# 단 대야 속의 빨래가 끝난 후 새로운 빨래를 시작할 수 있다
# 가장 긴 시간이 걸리는 빨래부터 시작
# 그 다음 긴 시간이 걸리는 빨래와 함께 세탁
# 이것을 반복


def min_wash_time(list):
    # 오름차순 정렬
    s_list = sorted(list)
    total = 0

    while len(s_list) > 0:
        max_n = s_list.pop()
        total += max_n
        if len(s_list) > 0:
            s_list.pop()
        else:
            return total

    return total


print(total_wash_time(clothes_dic))
