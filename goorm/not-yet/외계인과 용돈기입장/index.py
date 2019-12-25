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
		
