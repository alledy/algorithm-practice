user_input = input()

# 공백 기준으로 스플릿해서 리스트에 담기
my_list = user_input.split()

# max와 min 으로 대소 비교 후 int로 형변환
a = int(max(my_list))
b = int(min(my_list))


def gcd(a, b):

    r = a

    while r > 0:
        r = a % b
        if r == 0:
            return b
        else:
            a = b
            b = r


print(gcd(a, b))
