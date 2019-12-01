# [최소값](https://level.goorm.io/exam/43125/%EC%B5%9C%EC%86%8C%EA%B0%92/quiz/1)

## 포인트
- 리스트 중 가장 작은 원소를 출력하는 아주 간단한 문제인데, 문제는 인풋이 str으로 들어와서 int로 바꿔야 하는 부분이다. 
- 그래서 for 문으로 아래처럼 돌리면 될 줄 알았는데 이렇게 하면 int형으로 변환이 안된다. 
```py
my_list = ['-2','-1', '1', '3']
for i in my_list:
    i = int(i)

print(type(my_list[0])) # <class 'str'>
print(min(my_list)) # -1
```
- 처음에는 그냥 my_list의 원소인 i를 불러서 거기에 int(i)를 재할당했으니 my_list 내부 원소들이 다 int형으로 바뀌어서 재할당 됐을 줄 알았다. 하지만 여기서 i는 그냥 my_list안의 원소 값을 복사하여 갖고 있는 것뿐이므로, i가 함수 내부에서 변화된다고 해서 실제 my_list 내부에 있는 값은 변하지 않는다. (__call by value__ 와 비슷하다. 파이썬이라서 정확히 call by value라고는 말할 수 없다:confused:) 
```py
my_list = ['-2','-1', '1', '3']
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

print(type(my_list[0])) # <class 'str'>
print(min(my_list)) # -1
```
- 위처럼 my_list에 인덱스로 접근하여 재할당하면, 함부 내부에서 변화돼었어도 실제 메모리에 저장된 값이 변경되기 때문에 int형으로 변화된 것을 알 수 있다. (__call by reference__ 와 비슷하다. 이 역시 파이썬에서는 정확한 용어가 아니다:confused:) 
- 아니면 list comprehension으로 아예 새로운 리스트를 만들어 int형으로 변환된 원소를 넣을 수 있다. 아래에서 my_list라는 변수명은 똑같아 보이지만, list comprehension으로 새로운 리스트를 만든 것이기 때문에 실제로는 다른 주소를 참조한다. 
```py
my_list = ['-2','-1', '1', '3']
my_list = [int(i) for i in my_list]

print(type(my_list[0])) # <class 'int'>
print(min(my_list)) # -2
```
- 아주 간단한 문제였지만 실수하면 안되므로 **주의**하자. 
  
## [풀이](./index.py)