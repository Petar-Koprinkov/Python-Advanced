from collections import deque

string_expression = deque(input().split(" "))
queue = deque()

while True:
    if string_expression[-1] not in "+-*/":
        break
    if string_expression[0] not in "+-*/":
        queue.append(string_expression.popleft())
    else:
        operator = string_expression.popleft()
        while len(queue) > 1:
            if operator == "-":
                result = int(queue.popleft()) - int(queue.popleft())
                queue.appendleft(result)
            elif operator == "+":
                result = int(queue.popleft()) + int(queue.popleft())
                queue.appendleft(result)
            elif operator == "/":
                result = int(queue.popleft()) // int(queue.popleft())
                queue.appendleft(result)
            elif operator == "*":
                result = int(queue.popleft()) * int(queue.popleft())
                queue.appendleft(result)
            if len(queue) == 1:
                string_expression.appendleft(str(result))
                queue = deque()

print(string_expression[0])







