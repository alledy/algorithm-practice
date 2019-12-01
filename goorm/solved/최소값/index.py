user_input = input()
my_str = input()
my_list = my_str.split(' ')
my_list = [int(i) for i in my_list]

print(min(my_list))
