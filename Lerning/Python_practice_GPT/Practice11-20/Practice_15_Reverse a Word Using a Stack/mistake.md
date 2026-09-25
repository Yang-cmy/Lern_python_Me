# Practice 15 — Reverse a Word Using Stack

## My Goal

The goal was to reverse a word using a **Stack**.

Example:

```text
Hello
```

should become:

```text
olleH
```

The Stack is useful because it follows:

**LIFO — Last In, First Out**

The last character pushed into the Stack will be the first character popped out.

---

# My Original Code

```python
def reverse_word(word):
    stack = []
    stack1 = []

    for c in word:
        stack.append(c)

    for c in range(len(stack)):
        last_char = stack.pop()
        stack1.append(last_char)

    return stack1
```

My Stack logic was correct, but there was one problem.

---

# Mistake 1 — Returning a List Instead of a String

My original code returned:

```python
return stack1
```

For:

```python
reverse_word("Hello")
```

this returns:

```python
["o", "l", "l", "e", "H"]
```

The characters are in the correct reversed order, but the result is a **list**.

What I actually want is:

```text
olleH
```

which is a **string**.

So I need to combine the characters using:

```python
"".join(stack1)
```

Therefore:

```python
return "".join(stack1)
```

---

# Understanding `join()`

Suppose I have:

```python
stack1 = ["o", "l", "l", "e", "H"]
```

This:

```python
"".join(stack1)
```

means:

> Join every element together using an empty string `""` between them.

Result:

```text
olleH
```

If I used:

```python
"-".join(stack1)
```

I would get:

```text
o-l-l-e-H
```

So the string before `.join()` determines what goes between the elements.

---

# How My Stack Works

Starting with:

```text
Hello
```

The first loop is:

```python
for c in word:
    stack.append(c)
```

Each character is pushed onto the Stack:

```text
H → ["H"]

e → ["H", "e"]

l → ["H", "e", "l"]

l → ["H", "e", "l", "l"]

o → ["H", "e", "l", "l", "o"]
```

The top of the Stack is:

```text
["H", "e", "l", "l", "o"]
                         ↑
                        TOP
```

---

# Popping the Stack

The second loop:

```python
for c in range(len(stack)):
    last_char = stack.pop()
    stack1.append(last_char)
```

removes characters from the top.

First:

```text
pop() → "o"

stack:
["H", "e", "l", "l"]

stack1:
["o"]
```

Then:

```text
pop() → "l"

stack1:
["o", "l"]
```

Then:

```text
pop() → "l"

stack1:
["o", "l", "l"]
```

Then:

```text
pop() → "e"

stack1:
["o", "l", "l", "e"]
```

Finally:

```text
pop() → "H"

stack1:
["o", "l", "l", "e", "H"]
```

Because Stack follows **LIFO**, the characters automatically come out in reverse order.

---

# Why `range(len(stack))` Works Here

Before the second loop starts:

```python
len(stack)
```

for `"Hello"` is:

```text
5
```

Therefore:

```python
range(len(stack))
```

becomes:

```python
range(5)
```

which runs the loop 5 times.

Even though `pop()` makes the Stack smaller during the loop, `range(5)` has already been created for this loop.

So:

```text
Loop 1 → pop
Loop 2 → pop
Loop 3 → pop
Loop 4 → pop
Loop 5 → pop
```

All five characters are removed.

---

# Correct Code

```python
def reverse_word(word):
    stack = []
    stack1 = []

    for c in word:
        stack.append(c)

    for c in range(len(stack)):
        last_char = stack.pop()
        stack1.append(last_char)

    return "".join(stack1)
```

Example:

```python
print(reverse_word("Hello"))
```

Output:

```text
olleH
```

---

# What I Did Correctly

I correctly understood the main Stack operations.

### PUSH

```python
stack.append(c)
```

Adds a character to the top of the Stack.

### POP

```python
stack.pop()
```

Removes the most recently added character.

### LIFO

```text
Input:
H e l l o

PUSH:
["H", "e", "l", "l", "o"]
                         ↑ TOP

POP order:
o
l
l
e
H

Result:
olleH
```

---

# What I Learned

My algorithm can be correct while my **return value is still the wrong data type**.

These are different:

```python
["o", "l", "l", "e", "H"]
```

This is a:

```text
list
```

while:

```python
"olleH"
```

is a:

```text
string
```

I should always think about:

```text
1. Is my algorithm correct?
2. Is the final value correct?
3. Is the final data type correct?
```

# Practical Rule

**Always check what data type the function is supposed to return.**

For this problem:

```text
PUSH characters → POP in reverse → JOIN characters → RETURN string
```

Or:

```python
append()       # PUSH
pop()          # POP
"".join(...)   # list of characters → string
```
