def decimal_to_binary(number):
    stack = []

    while number > 0:
        remain = number % 2
        number = number // 2

        stack.append(remain)

    results = ""

    while len(stack) > 0:
        last_binary = stack.pop()
        results += str(last_binary)

        # or just using this results += str(stack.pop())


    return results

print(decimal_to_binary(13))