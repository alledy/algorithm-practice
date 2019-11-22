# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import re

uid = input().strip()
pw1 = input().strip()
pw2 = input().strip()


def len_of_pattern(reg, pwd):
    my_list = re.findall(reg, pwd)
    if len(my_list) == 0:
        return 0
    find_str = ''.join(my_list)
    return len(find_str)


def check_pass(pwd):
    alp = r'[a-zA-Z]'
    num = r'[0-9]'
    sym = r'[!@#$]'

    alp_len = len_of_pattern(alp, pwd)
    num_len = len_of_pattern(num, pwd)
    sym_len = len_of_pattern(sym, pwd)

    # 알파벳 개수 > 0
    # 숫자 개수 > 0
    # 특수문자 개수 > 0
    # 모두 합친 숫자 >= 8 and <= 20
    # 모두 합친 숫자 == 패스워드 전체 길이
    # 위 5가지 조건 모두 충족하면 True, 아니면 False
    if not alp_len > 0:
        return False
    if not num_len > 0:
        return False
    if not sym_len > 0:
        return False

    total_len = alp_len + num_len + sym_len

    if not (total_len >= 8 and total_len <= 20):
        return False
    if not total_len == len(pwd):
        return False

    return True


def check_id(uid):
    id_p = r'^[0-9a-z]{3,20}$'
    if re.match(id_p, uid):
        return True
    return False


def check_same(pwd1, pwd2):
    if pwd1 == pwd2:
        return True
    else:
        return False


def signup_test(uid, pw1, pw2):
    # id 체크
    # pw1 체크
    # pw1 == pw2 체크
    if check_id(uid) == False:
        return "fail"
    if check_pass(pw1) == False:
        return "fail"
    if check_same(pw1, pw2) == False:
        return "fail"
    return "pass"


print(signup_test(uid, pw1, pw2))
