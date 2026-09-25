# Python Practice #11 — Build Your Own Stack

Your Week 4 material is now about Stack, especially LIFO, push, pop, peek, isEmpty, and implementing a stack with a Python list.

## Task

Create a class called Stack.

It should contain an internal list:

`self.items = []`

Then create these four methods:

```python
push(item)
pop()
peek()
is_empty()
```
Your methods should behave like this:

- push(item) → add an item to the top of the stack.
- pop() → remove and return the top item.
- peek() → return the top item without removing it.
- is_empty() → return True if the stack is empty, otherwise False.

Then test your class using:

```python
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())
print(stack.pop())
print(stack.peek())
```

## Expected output:

```python
30
30
20
```
Your course notes specifically describe Python's append() as the equivalent of push, pop() as removing the top item, and [-1] as accessing the top item. They also warn about underflow when trying to pop from an empty stack.

## Extra requirement

Make your `pop()` and `peek()` safe.

If the stack is empty, they should return:

```python
None
```

instead of crashing.

For this exercise, do not use a separate top variable yet. Let the Python list handle the stack position.

## Debugging challenge

After your program works, temporarily write:

`print(stack.items)`

after every operation and watch how the stack changes:
```python
[]
[10]
[10, 20]
[10, 20, 30]
[10, 20]
```

**Remember: the rightmost element is the top.**