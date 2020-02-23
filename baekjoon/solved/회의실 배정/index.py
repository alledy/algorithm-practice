import sys

with open('1931.txt', 'r') as sys.stdin:

    n = int(input())
    temp = sys.stdin.readline().split()
    arr = [(int(temp[0]), int(temp[1]))]
    for i in range(n-1):
        my_input = sys.stdin.readline().split()
        arr.append((int(my_input[0]), int(my_input[1])))

    arr = sorted(arr, key=lambda time: [time[1], time[0]])
    print(arr)
    """가장 이른 회의 끝나는 시간"""
    t = arr[0][1]
    count = 1
    for i in range(1, n):
        if arr[i][0] >= t:
            count += 1
            t = arr[i][1]

    print(count)
