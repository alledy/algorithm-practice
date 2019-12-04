# [Insertion Sort](https://level.goorm.io/exam/43085/insertion-sort/quiz/1)

## 포인트
- 출력 요구하는 형식: list가 아니라 원소 한 개씩 출력
- **temp의 존재**
  - 패스스루마다 비교/교환이 일어나는데, 이 때 비교의 기준이 되는 원소가 `list[start_index]`이다(최초에는)
  - 그런데 비교를 하고 나서 그 위치로 다른 원소를 옮겨버리기 때문에, `list[start_index]` 값은 고정돼있지 않다. 
  - 변경되기 전의 `list[start_index]`와 비교해야 하므로 이 값을 temp에 넣어 두고 비교 및 교환을 시작해야 한다. 

## [풀이](./index.py)