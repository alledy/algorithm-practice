import math

user_input = input()

my_list = user_input.split(' ')

fare_plan = int(my_list[0])
usage = int(my_list[1])
data_plan = {29900: 300, 34900: 1000,
             39900: 2000, 49900: 6000, 59900: 11000, 69900: math.inf}


def better_fare_plan(data_plan, fare_plan, usage):
    fare = list(data_plan.keys())
    data = list(data_plan.values())
    data_range = []
    # Mutable sort. 작은 순 -> 큰 순으로 정렬.
    fare.sort()

    for i in range(len(fare)-1):
        excess_data = (fare[i+1] - fare[i]) / 20
        data_range.append(data[i] + excess_data)

    for i in range(len(data_range)):
        if usage <= data_range[i]:
            return fare[i]

    return fare[-1]


def fare_calc(data_plan, fare_plan, usage):

    if fare_plan == 69900:
        return 69900

    data_limit = data_plan[fare_plan]

    if usage <= data_limit:
        return fare_plan

    excess = usage - data_limit

    if (excess >= 1250) and (excess < 5000):
        return fare_plan + 25000
    else:
        return fare_plan + min([20 * excess, 180000])


better_plan = better_fare_plan(data_plan, fare_plan, usage)
print(better_plan, end=" ")
print(fare_calc(data_plan, fare_plan, usage), end=" ")
print(fare_calc(data_plan, better_plan, usage))
