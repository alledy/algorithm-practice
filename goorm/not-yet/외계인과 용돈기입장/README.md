# [외계인과 용돈기입장](http://level.goorm.io/exam/49111/%EC%99%B8%EA%B3%84%EC%9D%B8%EA%B3%BC-%EC%9A%A9%EB%8F%88%EA%B8%B0%EC%9E%85%EC%9E%A5/quiz/1)

## 개선

### 일일이 계산 - TimeOut
- 처음에 짠 코드는 인덱스를 아규먼트로 받을 때마다 새로이 계산
- 타임아웃
  
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

### 탑다운 메모이제이션 - Runtime Error
- 탑다운 방식으로 저장, Runtime Error 발생
  
```python
user_input = input().split(' ')
# total days
n = int(user_input[0])
# total ranges
m = int(user_input[1])

# 인덱스 맞추기 위해 앞에 원소 삽입
account = input().split(' ')
account = [0] + [int(i) for i in account]

memo = {}


def print_account(acc, m):
    for i in range(m):
        str_list = input().split(' ')
        start = int(str_list[0])
        end = int(str_list[1])

        answer = calc(memo, start, end, acc)

        if answer > 0:
            print('+'+str(answer))
        else:
            print(answer)


def calc(memo, start, end, acc):
    if (start, end) in memo:
        return memo[(start, end)]

    if start == end:
        memo[(start, end)] = acc[start]
        return memo[(start, end)]

    memo[(start, end)] = calc(memo, start, end-1, acc) + acc[end]
    return memo[(start, end)]


print_account(account, m)
```

### 바텀업 메모이제이션
- 역시 똑같은 테케에서 런타임 에러😕 
```python
user_input = input().split(' ')
# total days
n = int(user_input[0])
# total ranges
m = int(user_input[1])

# 인덱스 맞추기 위해 앞에 원소 삽입
account = input().split(' ')
account = [0] + [int(i) for i in account]

memo = {}
def print_account(acc, m):
	for i in range(m):
		str_list = input().split(' ')
		start = int(str_list[0])
		end = int(str_list[1])
		
		answer = calc(memo, start, end, acc)
		
		if answer > 0:
			print('+'+str(answer))
		else:
			print(answer)
		

def calc(memo, start, end, acc):
	if (start, end) in memo:
		return memo[(start,end)]
	
	memo[(start,start)] = acc[start]
	
	for i in range(1, end-start+1):
		memo[(start, start+i)] = memo[(start, start+i-1)] + acc[start+i]
	
	return memo[(start,end)]

print_account(account, m)
```

- 아직 모르겠다...