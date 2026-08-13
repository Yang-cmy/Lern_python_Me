## Python Practice #19 — Stack with a Maximum Size

You've practiced normal `push()` and `pop()` operations. Now let's add another important stack concept: **overflow**.

### Task

Create a class called:

```python
class Stack:
```

The constructor should receive the maximum number of items the stack can hold:

```python
stack = Stack(3)
```

Inside the class, store:

```python
self.items = []
self.max_size = max_size
```

Create these four methods:

```python
push(item)
pop()
is_empty()
is_full()
```

### Rules

`is_empty()` should return:

```python
True
```

when there are no items.

`is_full()` should return `True` when:

```python
len(self.items) == self.max_size
```

`push(item)` should add the item only when the stack is **not full**. If it is full, print:

```text
Stack Overflow
```

`pop()` should remove and return the top item. If the stack is empty, print:

```text
Stack Underflow
```

and return `None`.

### Test your program

```python
stack = Stack(3)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
```

Expected output:

```text
Stack Overflow
30
20
10
Stack Underflow
None
```

Notice the two different problems:

```text
PUSH when FULL
      ↓
Stack Overflow

POP when EMPTY
      ↓
Stack Underflow
```

### Requirements

Use a **class**, a **list**, `append()`, `pop()`, `len()`, functions/methods, and conditions. Don't use external libraries.

### VS Code Debugging Challenge

Put a breakpoint inside `push()` and test:

```python
stack = Stack(2)

stack.push("A")
stack.push("B")
stack.push("C")
```

Watch:

```python
self.items
self.max_size
self.is_full()
```

Try to predict what happens to `self.items` when `"C"` is passed to `push()`.

### Your Turn

Send me **only your Python code**. I'll wait for your attempt before giving you a solution. Afterward, I'll explain any mistakes clearly and finish with **one practical rule to remember**.
