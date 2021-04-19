def solution(s):
    convert_count = 0
    count_zero = 0
    while s != "1":
        removed = list(filter(lambda x: x == "1", s))
        count_zero += len(s) - len(removed)
        s = format(len(removed), 'b')
        convert_count += 1
    return [convert_count, count_zero]