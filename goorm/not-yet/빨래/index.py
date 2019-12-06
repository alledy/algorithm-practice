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

# 해당 컬러의 옷 세탁에 걸리는 시간을 원소로 가진 리스트(eg. [5,5,5])


def min_wash_time(list):
    # 2개는 동시에 세탁할 수 있다
    # 2개가 있다면 최대 시간이 총 세탁 시간(eg. 3, 5 => 총 5 걸려 두 개 세탁)
    # 세탁물이 n개라서 2개씩 짝을 짓는다면(eg. (3,4),(5,6) => 6,4 총 10 걸려 4개 세탁)
    # 최대 시간과, 그 다음 2번째로 오래 걸리는 것을 하나로 묶는게 효율적
    # 소팅을 한 다음 홀수번째 인덱스 값 더하기(전체 길이가 홀수일 때는 마지막 원소값 더함)
    sorted_list = sorted(list)
    leng = len(sorted_list)
    total = 0
    i = 0

    if not leng > 0:
        return 0

    while i < leng-1:
        if i % 2 == 1:
            total += sorted_list[i]
        i += 1

    total += sorted_list[-1]
    return total


print(total_wash_time(clothes_dic))
