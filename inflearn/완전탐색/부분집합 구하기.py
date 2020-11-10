# 자연수 n이 주어지면 1부터 n까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램을 작성하시오

def main(n):
    ch = [0 for x in range(n+1)]
    print_subsets(1,n,ch) # ...1? 
    
def print_subsets(v,n,ch):
    if v == n+1:
        ans = []
        for i,x in enumerate(ch):
            if x == 1:
                ans.append(i)
        if len(ans) > 0 :
            print(ans)
        return
    ch[v] = 0
    print_subsets(v+1, n, ch)
    ch[v] = 1
    print_subsets(v+1, n, ch)

main(3)

"""
이건 상태트리를 작성하면 됨. 
원소 1을 넣을지 안넣을지, 원소 2를 넣을지 않넣을지...
이렇게 가지를 뻗어가다보면 완전이진트리가 나옴
트리 순회라고 생각하고 작성하면 좀 쉽게 접근할 수 있는 것 같음.
루트 노드가 0(안 넣음)일 때 왼쪽 서브 트리 순회, 루트 노트가 1일 때 오른쪽 트리 순회
"""