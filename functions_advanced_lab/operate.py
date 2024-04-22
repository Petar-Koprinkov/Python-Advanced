def operate(sign, *args):

    def add():
        return sum(args)

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result

    def subtraction():
        result = args[0]
        for index in range(1, len(args)):
            result -= args[index]
        return result

    def divide():
        result = args[0]
        for index in range(1, len(args)):
            result /= args[index]
        return result

    if sign == "+":
        return add()
    elif sign == "-":
        return subtraction()
    elif sign == "*":
        return multiply()
    elif sign == "/":
        return divide()


print(operate("/", 20, 4))
