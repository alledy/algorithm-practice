user_input = input()
my_list = user_input.split(' ')
my_list = [int(i) for i in my_list]

# 해당 연월이 있는지 없는지 먼저 체크
# 없으면 에러
# 해당 연월을 하나의 숫자로 convert 후
# 7로 나눈 나머지를 요일 배열의 인덱스로 접근

month_day = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def convert_to_total(m,d):
	total = 0
	
	for i in range(1,m):
		total += month_day.get(i)
	
	total += d
	
	return total

def get_day(list):
	day = ['THR', 'FRI', 'SAT', 'SUN', 'MON', 'THU', 'WED']
	
	m = list[0]
	d = list[1]
	
	# 에러가 나는 경우
	if m > 12 or m < 1:
		return 'ERROR'
	if d > month_day.get(m) or d < 1:
		return 'ERROR'
	
	total = convert_to_total(m,d)
	r = total % 7
	
	return day[r]

print(get_day(my_list))
	