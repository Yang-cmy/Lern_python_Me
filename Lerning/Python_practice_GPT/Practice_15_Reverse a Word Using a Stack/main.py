def reverse_word(word):
    stack = []
    stack1 = []
    for c in word:
        stack.append(c)

    for c in range(len(stack)):
        last_char = stack.pop()
        stack1.append(last_char)
    
    return "".join(stack1)

print(reverse_word("Python"))
print(reverse_word("Stack"))
print(reverse_word("ABC"))