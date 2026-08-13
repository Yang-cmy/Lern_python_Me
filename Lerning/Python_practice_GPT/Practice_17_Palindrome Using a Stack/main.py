def is_palindrome(word):
    stack = []
    for c in word:
        print(c)
        stack.append(c)

    reverse = ""

    for c in word:
        last_word = stack.pop()
        reverse += last_word
    
    return reverse.upper() == word.upper()
    
    

print(is_palindrome("level"))
    