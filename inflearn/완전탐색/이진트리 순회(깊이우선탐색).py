# 조각으로 나누기: 루트, 왼, 오
# 기저조건
# 필요입력: 루트 노드

# 완전 이진 트리 순회
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def pre_order(root):
    if root.val == None:
        return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if root:
        in_order(root.left)
        print(root.val)
        in_order(root.right)
        
def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val)


