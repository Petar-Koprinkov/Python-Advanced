from collections import deque

text = deque(input())

while text:
    print(text.pop(), end="")