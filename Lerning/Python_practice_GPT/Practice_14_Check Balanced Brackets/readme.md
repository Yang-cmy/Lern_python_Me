# Python Practice #14 — Stack: Check Balanced Brackets

## Focus

- Stack
- Lists
- Loops
- Functions
- `push` / `pop`
- Debugging in VS Code

---

## Scenario

You're writing a small tool that checks whether brackets in a piece of code are balanced.

For example:

```text
(5 + 3)
```

is balanced.

But:

```text
(5 + 3
```

is **not** balanced because `(` was never closed.

---

## Your Task

Write a function:

```python
def check_brackets(text):
```

The function receives a string and uses a **list as a stack**.

For now, you only need to handle:

```text
(
)
```

---

## Rules

When your loop finds:

```text
(
```

push it onto the stack using:

```python
stack.append(...)
```

When your loop finds:

```text
)
```

remove one `(` from the stack using:

```python
stack.pop()
```

But be careful:

If you find `)` when the stack is already empty, the brackets are incorrect.

---

## Examples

### Example 1

```python
print(check_brackets("(5 + 3)"))
```

Expected:

```text
True
```

### Example 2

```python
print(check_brackets("((10 + 5) * 2)"))
```

Expected:

```text
True
```

### Example 3

```python
print(check_brackets("(10 + 5"))
```

Expected:

```text
False
```

### Example 4

```python
print(check_brackets("10 + 5)"))
```

Expected:

```text
False
```

---

## Requirements

Your program must:

- Create an empty list called `stack`.
- Use a `for` loop to examine the characters.
- Use `append()` as **push**.
- Use `pop()` as **pop**.
- Prevent `pop()` from being used on an empty stack.
- Return either `True` or `False`.

Do **not** use:

```python
text.count("(")
text.count(")")
```

The goal is to solve it using **Stack logic**.

---

## Think About This

At the end of the loop:

```python
stack = []
```

What should that tell you?

And what if:

```python
stack = ["(", "("]
```

What does that mean?

---

## VS Code Debugging Challenge

Put a breakpoint inside your `for` loop.

Run:

```python
check_brackets("(()")
```

Press:

```text
F10
```

for each iteration and watch:

```python
character
stack
```

You should see something similar to:

```text
character = "("
stack = ["("]

character = "("
stack = ["(", "("]

character = ")"
stack = ["("]
```

Ask yourself:

**Why is there still one item in the stack when the loop finishes?**

---

# Your Turn

Write the function yourself.

Send me **only your Python code** when you're finished.

I won't show the solution before your attempt. After you answer, I'll explain any mistakes clearly and finish with **one practical rule to remember**.