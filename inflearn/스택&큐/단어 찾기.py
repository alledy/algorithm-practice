# preword는 n개 arr
# useword는 n-1개 arr
# 안겹치는거 하나 찾기
def find_word(pre_word, use_word):
    pre = {}
    for x in pre_word:
        # 만약 x 키가 없을 경우 default 값 0으로 해주는 syntax
        pre[x] = pre.get(x, 0) + 1
    for x in use_word:
        pre[x] = pre.get(x) - 1
    for x in pre:
        if pre[x] == 1:
            return x
            
            
        
        
    