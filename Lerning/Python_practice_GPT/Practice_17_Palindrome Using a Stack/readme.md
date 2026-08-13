## Python Practice #17 — Palindrome Checker Using a Stack

Let's continue your **Stack** practice. This time you'll combine a **list, loops, functions, and LIFO** to determine whether a word is a palindrome.

A **palindrome** reads the same forward and backward.

Examples:

```text
level
radar
madam
```

But:

```text
python
hello
```

are not palindromes.

### Task

Write a function:

```python
def is_palindrome(word):
```

Your function should:

1. Create an empty list called `stack`.
2. Use a `for` loop to push every character of `word` onto the stack.
3. Use another loop to `pop()` characters from the stack.
4. Build a reversed version of the word.
5. Compare the original word with the reversed word.
6. Return `True` or `False`.

### Example

```python
print(is_palindrome("level"))
print(is_palindrome("python"))
print(is_palindrome("radar"))
```

Expected output:

```text
True
False
True
```

### Requirements

Use:

```python
stack.append(...)
stack.pop()
```

and at least:

* One list
* One function
* Two loops

Don't use Python's shortcuts:

```python
word[::-1]
reversed(word)
```

The point is to understand how a **stack reverses the order of data**.

### Extra Challenge

Make uppercase and lowercase letters count as the same:

```python
print(is_palindrome("Level"))
```

should produce:

```text
True
```

You can use:

```python
word.lower()
```

for this part.

### VS Code Debugging Challenge

Test:

```python
is_palindrome("CAT")
```

Put a breakpoint inside the loop containing `pop()` and watch:

```text
stack
reversed_word
```

You should see:

```text
stack                 reversed_word

["C", "A", "T"]       ""
["C", "A"]            "T"
["C"]                 "TA"
[]                    "TAC"
```

Notice what happened: even though you pushed `C → A → T`, you got them back as `T → A → C`.

That's **LIFO** doing the work.

### Your Turn

Send me **only your Python code**.

I'll wait for your solution first. Then I'll review it, explain any mistakes clearly, and finish with **one practical rule to remember**.
