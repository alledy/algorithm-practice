user_input = input()
# 괄호 하나씩 split해서 리스트에 저장
my_list = list(user_input)

# 여는 괄호일 때는 스택에 push
# 닫는 괄호라면 스택의 마지막 원소를 읽어 여는 괄호와 짝이 맞는지 확인
# 짝이 맞으면 스택에서 마지막 원소 pop
# my_list 순회가 끝났을 때 스택도 비어있는지 확인


def my_stack(my_list):
    open_bracket = {'{': '}', '[': ']', '(': ')'}
    close_bracket = {'}': '{', ']': '[', ')': '('}
    stack = []
    for i in my_list:
        if i in open_bracket:
            stack.append(i)
        elif i in close_bracket:
            if stack[-1] == close_bracket[i]:
                stack.pop()
            else:
                return False

    if not len(stack) == 0:
        return False

    return True


print(my_stack(my_list))
