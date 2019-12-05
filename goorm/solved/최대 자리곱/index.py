n_str = input()

# 앞자리 수를 낮추면 뒷자리 수가 9까지 가능
# 큰 자리 수부터 하나씩 낮춰서 그 뒤를 9로 해서 계산해보면
# N자리 수인 경우 총 N가지 가짓 수가 나온다

# 일단 N가지 수를 만드는 것 - calc_n
# 그 다음은 각 수의 곱을 계산 - calc_mul
# 가장 큰 수를 도출 - find_biggest_mul


def find_biggest_mul(n):
    # 여기서 n은 스트링형으로 iterable하다
    biggest = calc_mul(n)
    # i는 -1할 인덱스
    for i in range(len(n)-1):
        temp = calc_n(n, i)
        temp_mul = calc_mul(temp)
        if temp_mul > biggest:
            biggest = temp_mul

    return biggest


def calc_n(n, i):
    # 여기서 n은 스트링형으로 iterable하다
    # 인덱스 i까지 자른후 int 변환

    temp = int(n[:i+1])
    temp = temp - 1

    if temp == 0:
        new_n = '9' * len(n[i+1:])
    else:
        new_n = str(temp) + ('9' * len(n[i+1:]))

    return new_n


def calc_mul(n):
    # 여기서 n은 스트링형으로 iterable하다
    result = 1
    for i in range(len(n)):
        temp = int(n[i])
        result *= temp

    return result


print(find_biggest_mul(n_str))
