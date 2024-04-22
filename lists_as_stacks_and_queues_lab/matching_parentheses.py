from collections import deque

expression = input()
open_stack = deque()


for index in range(len(expression)):
    if expression[index] == "(":
        open_stack.append(index)
    elif expression[index] == ")":
        open_index = open_stack.pop()
        close_index = index + 1
        print(expression[open_index:close_index])






