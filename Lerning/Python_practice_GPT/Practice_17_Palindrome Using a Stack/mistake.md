# Practice 17 — Palindrome Using a Stack

## Score: 9/10

My solution was correct. I successfully used a Stack to reverse the word and compare it with the original.

## What I Did Well

I correctly used:

```python
stack.append(c)
```

to **PUSH** every character onto the Stack.

Then:

```python
stack.pop()
```

to **POP** characters in reverse order.

I also correctly built the reversed word:

```python
reverse += last_word
```

And using:

```python
reverse.upper() == word.upper()
```

allows `"Level"` and `"level"` to be treated the same.

## Small Mistake — Unnecessary `str()`

I wrote:

```python
last_word = str(stack.pop())
```

But every character from `word` is already a string.

For example:

```python
stack = ["l", "e", "v", "e", "l"]
```

`stack.pop()` already returns:

```python
"l"
```

So this is enough:

```python
last_word = stack.pop()
```

## Part That Can Be Improved

I wrote:

```python
if reverse.upper() == word.upper():
    return True
else:
    return False
```

This is correct, but the comparison itself already produces `True` or `False`.

So it can be shortened to:

```python
return reverse.upper() == word.upper()
```

## Improved Code

```python
def is_palindrome(word):
    stack = []

    for c in word:
        stack.append(c)

    reverse = ""

    for c in word:
        last_word = stack.pop()
        reverse += last_word

    return reverse.upper() == word.upper()


print(is_palindrome("level"))
print(is_palindrome("python"))
print(is_palindrome("radar"))
```

Output:

```text
True
False
True
```

## Practical Rule

**If an expression already returns `True` or `False`, I can return the expression directly.**

Instead of:

```python
if condition:
    return True
else:
    return False
```

I can write:

```python
return condition
```
