# [외계인과 용돈기입장](http://level.goorm.io/exam/49111/%EC%99%B8%EA%B3%84%EC%9D%B8%EA%B3%BC-%EC%9A%A9%EB%8F%88%EA%B8%B0%EC%9E%85%EC%9E%A5/quiz/1)

## 개선 과정

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

### 다른 동적프로그래밍(?)
- 이 문제의 특징은 인풋의 범위가 굉장히 크다는 점이다. 외계인이 요청할 수 있는 계산의 횟수가 $2*10^5$까지 가능하다. 
- 그래서 계산의 양을 줄이기 위해 메모이제이션을 했지만, 탑다운이든 바텀업이든 런타임에러가 났다. 결국 메모리를 너무 많이 써서 그런 듯 했다.
- 이 문제를 푸는 방법은 첫번째부터 n번째까지의 수입/지출을 모두 더한 값을 갖고 있는 것이다. 
  - 만약 3 5가 인풋으로 들어왔다면, 1~5까지 합한 값에서 1~2까지 합한 값을 빼면 된다.
  -  그러므로 1~1, 1~2, 1~3, 1~4, ..., 1~n 까지의 합을 모두 저장해놓으면(`sum_from_start`), 연산은 O(1)만 걸린다. 
  -  이 때 저장하는 것도 n만큼의 메모리만 차지하면 되므로 효율적이다. 반면 내가 위에서 딕셔너리로 메모이제이션을 하려고 했을 때는 약 $n^2/2$만큼의 메모리를 차지할 수 있다. start와 end값을 튜플로 만들어 저장했기 때문이다. (단 end >= start)

## [풀이](./index.py)