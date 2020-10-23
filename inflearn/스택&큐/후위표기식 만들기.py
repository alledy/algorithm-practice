# def get_postfix(pref):
#     stack = []
#     ans = ''
#     for x in pref:
#         if x.isdecimal():
#             ans += x
#         else:
#             if x == '*' or x == '/': 
#                 while stack and (stack[-1] == '*' or stack[-1] == '/'):
#                     ans += stack.pop()
#                 stack.append(x)
#             elif x == '+' or x == '-':
#                 while stack and (stack[-1] == '+' or stack[-1] == '-'):
#                     ans += stack.pop()
#                 stack.append(x)
#             elif x == '(':
#                 stack.append(x)
#             elif x == ')':


                    

