user_input = input()

my_list = user_input.split(' ')

fare_plan = int(my_list[0])
usage = int(my_list[1])

def better_fare_plan(fare_plan, usage):
	if usage <= 550:
		return 29900
	elif (usage > 500) & (usage <= 1250):
		return 34900
	elif (usage > 1250) & (usage <= 2500):
		return 39900
	elif (usage > 2500) & (usage <= 6500):
		return 49900
	elif (usage > 6500) & (usage <= 11500):
		return 59900
	else:
		return 69900
	
def fare_calc(fare_plan, usage):
	data_plan = {29900: 300, 34900: 1000, 39900: 2000, 49900: 6000, 59900: 11000}
	
	if fare_plan == 69900:
		return 69900
	
	data_limit = data_plan[fare_plan]
	
	if usage > data_limit:
		excess = usage - data_limit
		if (excess >= 1250) & (excess < 5000): 
			return fare_plan + 25000
		else:
			total = fare_plan + (20 * excess)
			return min([total, 180000])
	else:
		return fare_plan
	
better_plan = better_fare_plan(fare_plan, usage)	
print(better_plan, end=" ")
print(fare_calc(fare_plan, usage), end=" ")
print(fare_calc(better_plan, usage))
