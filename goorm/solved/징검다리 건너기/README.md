# [징검다리 건너기](https://level.goorm.io/exam/49112/%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC-%EA%B1%B4%EB%84%88%EA%B8%B0/quiz/1)

## 포인트
- recursive(`Top-Down`) 말고 for loop(`Bottom-Up`)으로 풀기
  - 처음에는 recursive로 풀었는데, Runtime Error 발생
  - recursionlimit을 올려도 해결이 안 돼서 for loop으로 풀어야 한다
  - 아래는 탑다운 방식으로 풀었다가 런타임 에러 난 코드
    ```python
    import sys
    # Runtime Error
    sys.setrecursionlimit(100000000)

    total_n = int(input())
    str_list = input().split(' ')
    n_list = [int(i) for i in str_list]
    my_list = [0] + n_list + [0]
    memo = {}

    # n번째까지의 최소로 묻을 수 있는 독의 총량

    def p(list, n):
        # 메모이제이션
        if n in memo:
            return memo[n]

        # 기저조건에서 return을 써줘야 함. 안 그러면 밑의 코드까지 실행하면서 Recursion Error
        if n == 1:
            memo[n] = list[n]
            return memo[n]

        if n == 2:
            memo[n] = list[n]
            return memo[n]

        if n == 3:
            memo[n] = list[n]
            return memo[n]

        memo[n] = min(p(list, n-1), p(list, n-2), p(list, n-3)) + list[n]

        return memo[n]


    print(p(my_list, len(my_list)-1))

    ```

## [풀이](./index.py)