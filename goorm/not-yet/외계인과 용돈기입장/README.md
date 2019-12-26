# [외계인과 용돈기입장](http://level.goorm.io/exam/49111/%EC%99%B8%EA%B3%84%EC%9D%B8%EA%B3%BC-%EC%9A%A9%EB%8F%88%EA%B8%B0%EC%9E%85%EC%9E%A5/quiz/1)

## 개선
- 타임아웃 나서 테스트케이스 절반 가량만 통과함. 
- 처음에 짠 코드는 인덱스를 아규먼트로 받아서 받을 때마다 새로이 계산
- 타임아웃 나서 메모이제이션했지만 여전히 타임아웃
  
```python
user_input = input().split(' ')
# total days
n = int(user_input[0])
# total ranges
m = int(user_input[1])

# 인덱스 맞추기 위해 앞에 원소 삽입
account = input().split(' ')
account = [0] + [int(i) for i in account]

for i in range(m):
	str_list = input().split(' ')
	start_i = int(str_list[0])
	end_i = int(str_list[1])
	total = 0
	for index in range(start_i, end_i+1):
		total += account[index]
	if total > 0:
		print('+'+str(total))
	else:
		print(total)
		
```