# [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## 풀이법
- 유형: `DP`
- 점화식: `f(n) = (f(n-1) > 0 ? f(n-1) : 0) + nums[n-1]` 
  
  DP는 점화식을 생각해내는 게 제일 중요하다. (맨 처음에는 DP라고 생각 안하고 이중 for문을 돌려서 O(n^2) 으로 풀었더니 타임 에러가 났다.) 원소를 하나씩 늘려 나갈 때 매번 새로운 sum을 구하지 않고 그 전까지의 sum이 0보다 큰지 검사해서 양수이면 더하고, 아니면 해당 인덱스 원소만 sum으로 저장한다.

## [풀이](./index.py)