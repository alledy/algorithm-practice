# [빨래](http://level.goorm.io/exam/43229/%EB%B9%A8%EB%9E%98/quiz/1)

## 주의
- 문제를 처음에 잘못 이해함. 
- 이게 처음에 푼 코드인데, 색깔 별로 빨래 시간을 담은 리스트를 인자로 받아, 최소 빨래 시간을 리턴하는 함수이다.
- 그런데 나는 [4,5,6] 이라는 리스트가 들어오면, 가장 긴 6시간이 걸리는 빨래를 할 때, 5를 하고 나서 1시간이 남으니까 이 때 4짜리 빨래를 시작해도 되는 줄 알았다. 그러면 4에서 1시간을 빼서 뒤에 3시간만 더 하면 끝나는 것이라고 생각했다. 
- 하지만 문제에는 분명히 `대야 속 빨래가 끝난 이후 새로운 빨래를 시작할 수 있습니다` 라고 쓰여 있다. 
- 즉 내가 문제를 오히려 더 복잡하게 생각한 것. 
- 역시 문제를 꼼꼼이 읽어야 한다.
   
```python
# 잘못 푼 코드
def min_wash_time(list):
    # 내림차순 정렬
    s_list = sorted(list, reverse=True)
    total = 0

    while len(s_list) > 0:
        biggest = s_list.pop(0)
        total += biggest
        while biggest > 0 and len(s_list) > 0:
            if biggest > s_list[0]:
                biggest -= s_list.pop(0)
            else:
                s_list[0] -= biggest
                biggest = 0

    return total
```



## [풀이](./index.py)