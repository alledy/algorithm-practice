# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
total_io = int(input())

# 최대 10 개의 자료 가능

q = []
cnt = 0

# d 또는 D - 출력
# e 또는 E - 입력
e = ('e', 'E')
d = ('d', 'D')

# e 또는 d가 들어오는 횟수를 세어 total_io에 달하면 종료
while cnt < total_io:
    i = input()
    if i in e:
        input_val = input()
        if len(q) < 10:
            q.append(input_val)
        else:
            print("overflow")

    elif i in d:
        if len(q) > 0:
            q = q[1:]
        else:
            print("underflow")

    else:
        break

    cnt += 1

for i in q:
    print(i, end=" ")
