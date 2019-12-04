n = input()
str_list = input().split(' ')
n_list = [int(i) for i in str_list]
find_n = int(input())


def binary_search(list, find_n):
    start_index = 0
    end_index = len(list)-1

    while start_index <= end_index:
        mid = (start_index + end_index) // 2

        if list[mid] == find_n:
            return mid+1

        if list[mid] > find_n:
            end_index = mid - 1

        if list[mid] < find_n:
            start_index = mid + 1

    return "X"


print(binary_search(n_list, find_n))
