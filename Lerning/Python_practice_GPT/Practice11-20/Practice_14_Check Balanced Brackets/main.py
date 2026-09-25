def check_brackets(text):
    stack = []
    target1 = "("
    target2 = ")"
    for l in text:
        if l == target1:
            stack.append(l)

        if l == target2:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False



print(check_brackets("(5 + 3)"))
print(check_brackets("((10 + 5) * 2)"))
print(check_brackets("(10 + 5"))
print(check_brackets("10 + 5)"))