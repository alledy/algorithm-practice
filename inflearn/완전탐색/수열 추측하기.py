"""
문제
1부터 n까지의 숫자가 첫번째 줄에 있다고 하자. 
3 1 2 4 이런 식으로. 
그리고 파스칼의 삼각형처럼 인접한 숫자 2개를 더한 값을 아래에 놓는다.
3  1  2  4
 4  3  6
  7  9
   16
이런 식으로 마지막에 숫자 하나가 나오게 된다. 
이 마지막 숫자와, n이 주어졌을 때에 가능한 맨 첫번째 줄을 출력하면 된다. 
예를 들어 4와 16이 주어졌을 때 3 1 2 4를 출력하면 된다. (답 여러개 가능, 여러개일 경우 사전순 출력)
"""

# input 배열
# output 아래 줄 배열
def next_row(arr):
   l = len(arr)
   output = []
   for i in range(l-1):
      output.append(arr[i] + arr[i+1])
   return output

def go_down(arr,original):
   if len(arr) == 1:
      if arr[0] == t:
         print(original)
      return
   else:
      go_down(next_row(arr),original)

# 첫번째줄에 1부터 n까지의 숫자
# 마지막에 나와야 하는 마지막 숫자 t
# 중복이 아닌 순열!!!

n,t=4,16
def permutation(pickable,picked,d):
   if d == n:
      original = picked
      go_down(picked,original)
      return
   for i in range(len(pickable)):
      rest = []
      for j in range(len(pickable)):
         if i != j:
            rest.append(pickable[j])
      picked.append(pickable[i])
      # 이 부분을 다른 사람은 어떻게 처리하려나?
      permutation(rest,picked,d+1)
      picked.pop()

permutation([1,2,3,4],[],0)


# ====================================================
# arr는 길이 n인 리스트
# ch는 넣었는지 아닌지 표시하는 리스트, 길이는 n+1
arr = [0 for x in range(n)]
ch = [0 for x in range(n+1)]
pool = [x for x in range(1,n+1)]
def permutation2(arr,d,ch):
   if d == len(arr):
      original = arr
      go_down(arr,original)
      return
   for x in pool:
      if ch[x] != 1: # 중복 순열과의 차이점
         arr[d] = x
         ch[x] = 1
         permutation2(arr,d+1,ch)   
         ch[x] = 0 # 여기도 pop처리와 같음!!!   

   
