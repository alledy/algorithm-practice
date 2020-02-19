import sys
# sys.setrecursionlimit(10000)
with open('1495.txt', 'r') as sys.stdin:

    input_list = sys.stdin.readline().split()
    n = int(input_list[0])
    s = int(input_list[1])
    m = int(input_list[2])
    v_list = sys.stdin.readline().split()
    v = [int(i) for i in v_list]

    """
    m 은 최대 볼륨
    n 은 곡의 개수
    s는 시작 볼륨
    v는 볼륨 차이 리스트 
    """

    def max_volume(s, n, m, v):
        memo = {n_list: [] for n_list in range(n)}
        memo[0].append(s)

        for i in range(n-1):
            prev_vol_list = memo[i]
            for j in prev_vol_list:
                small = calc_smaller(j, v[i])
                big = calc_bigger(j, m, v[i])

                if small != -1:
                    memo[i+1].append(small)
                if big != -1:
                    memo[i+1].append(big)

        for i in range(len(memo[n-1])):
            max = 0
            temp = memo[n-1][i]

            big_temp = calc_bigger(temp,  m, v[n-1])
            if big_temp == m:
                return m
            if big_temp > max:
                max = big_temp

            small_temp = calc_smaller(temp, v[n-1])
            if small_temp > max:
                max = small_temp

        return max

    def calc_smaller(num, diff):
        if num == 0:
            return -1
        elif num - diff <= 0:
            return 0
        else:
            return num - diff

    def calc_bigger(num, m, diff):
        if num == m:
            return -1
        elif num + diff >= m:
            return m
        else:
            return num + diff

    print(max_volume(s, n, m, v))
