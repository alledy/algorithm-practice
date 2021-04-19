from collections import Counter
from functools import reduce

def solution(clothes):
    kind_counts = Counter([kind for _, kind in clothes])
    return reduce(lambda acc, cur: acc * (cur + 1), kind_counts.values(), 1) - 1
        