def anagram(a1, a2):
    h = {}
    for x in a1:
        h[x] = h.get(x, 0) + 1
    for y in a2:
        h[y] = h.get(y,0) - 1
        if h.get(y) == 0:
            h.pop(y)
    if len(h) != 0:
        return False
    return True
    
anagram('AbaAeCe', 'baeeACA')

"""
이 문제는 아스키넘버로 풀 수도 있음 (리스트 해쉬)
[0]*52 해놓고 해당하는 문자열이 나올 떄 해당 인덱스 숫자 올리고 뺴는 식으로
알파벳을 아스키 넘버로 바꾸는 것 ord(x)
"""