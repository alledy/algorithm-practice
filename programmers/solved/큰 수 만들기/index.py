def solution(number, k):
    collected = []  # 문자열로 해도 되지만 문자열은 이뮤터블이고 리스트는 뮤터블이므로 효율이 더 좋다
    """
    index와 원소 모두 필요할 때 enumerate 사용
    for 문으로 돌면서 빼야 하는 조건인지, 더해야 하는 조건인지 판단
    빼야 하는 조건일 때는 while문으로 그 전까지 검사해야 한다
    """
    for i, num in enumerate(number):
        while len(collected) > 0 and k > 0 and collected[-1] < num:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    # 뒤에서 k개 자르기
    if k > 0:
        collected = collected[:-k]
    return ''.join(collected)
