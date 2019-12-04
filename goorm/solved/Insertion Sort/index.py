total_n = int(input())
str_list = input().split(' ')
n_list = [int(i) for i in str_list]
cnt = int(input())


def insertion_sort(list, cnt):

    # 총 cnt번 패스스루 진행
    for start_index in range(1, cnt+1):
        position = start_index
        temp = list[start_index]

        # 탈출 조건 - 배열의 왼쪽 끝까지 왔거나, 비교 원소가 더 작을 때
        while position > 0 and list[position-1] > temp:
            list[position] = list[position-1]
            position -= 1

        list[position] = temp

    return list


result = insertion_sort(n_list, cnt)
for i in result:
    print(i, end=" ")
